#!/usr/bin/env python3
"""Add Front/Back flashcards from a Markdown file to Anki via AnkiConnect.

Markdown format expected per card:

    ### Card 1
    **Front:** What is the internet?
    **Back:** A network of networks.

Usage:
    python3 anki_add_cards.py cards.md --deck "Topic" --tags topic tag2

Inline markdown in card text renders: `code` becomes code-styled text and
**bold** becomes bold.

After adding, the script places the deck's new cards in the file's order,
so the source's sequence becomes the study sequence (use --no-reposition
to skip). Cards that are already scheduled keep their scheduling.

Requires: Anki running, AnkiConnect add-on installed (default port 8765).
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import urllib.error
import urllib.request

DEFAULT_URL = "http://127.0.0.1:8765"
API_VERSION = 6


def invoke(action: str, url: str = DEFAULT_URL, **params):
    """Send one AnkiConnect request; raise on transport or API error."""
    payload = json.dumps({"action": action, "version": API_VERSION, "params": params}).encode("utf-8")
    request = urllib.request.Request(url, payload, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            body = json.load(response)
    except urllib.error.URLError as exc:
        raise SystemExit(f"Cannot reach AnkiConnect at {url} - is Anki running? ({exc})")

    if len(body) != 2 or "error" not in body or "result" not in body:
        raise SystemExit(f"Unexpected AnkiConnect response: {body!r}")
    if body["error"] is not None:
        raise RuntimeError(body["error"])
    return body["result"]


def render_field(text: str) -> str:
    """Escape HTML, then render the inline markdown cards use."""
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)


CARD_RE = re.compile(r"^###\s+Card\s+\d+\s*$", re.MULTILINE)
FRONT_RE = re.compile(r"^\*\*Front:\*\*\s*(.+?)\s*$", re.MULTILINE)
BACK_RE = re.compile(r"^\*\*Back:\*\*\s*(.+?)\s*$", re.MULTILINE)


def parse_flashcards(path: str) -> list[dict[str, str]]:
    """Return [{'front': ..., 'back': ...}, ...] for every `### Card N` block."""
    text = open(path, encoding="utf-8").read()
    headings = list(CARD_RE.finditer(text))
    cards = []
    for index, heading in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        block = text[heading.end():end]
        front = FRONT_RE.search(block)
        back = BACK_RE.search(block)
        if not front or not back:
            continue
        # Keep the raw text; make_note renders it into Anki's HTML fields.
        cards.append({
            "front": front.group(1).strip(),
            "back": back.group(1).strip(),
        })
    return cards


def make_note(card: dict[str, str], deck: str, tags: list[str], allow_duplicates: bool = False) -> dict:
    return {
        "deckName": deck,
        "modelName": "Basic",
        "fields": {"Front": render_field(card["front"]), "Back": render_field(card["back"])},
        "tags": tags,
        # Duplicate policy: refuse a new note whose first field already exists
        # for this note type anywhere in the collection. Add
        # {"duplicateScope": "deck"} to check only the target deck.
        "options": {"allowDuplicate": allow_duplicates},
    }


def reposition_cards(deck: str, ordered_fronts: list[str], url: str) -> None:
    """Put the deck's new cards into the file's order, after new cards from other sources."""
    card_ids = invoke("findCards", url=url, query=f'deck:"{deck}"')
    if not card_ids:
        return
    cards = invoke("cardsInfo", url=url, cards=card_ids)
    order_of = {render_field(front): index for index, front in enumerate(ordered_fronts)}

    file_cards = []
    other_positions = []
    for card in cards:
        front = card["fields"].get("Front", {}).get("value", "")
        is_new = card["type"] == 0 and card["queue"] == 0
        if front in order_of:
            file_cards.append((order_of[front], card["cardId"], is_new))
        elif is_new:
            other_positions.append(card["due"])

    new_cards = sorted(card for card in file_cards if card[2])
    if not new_cards:
        return
    scheduled = len(file_cards) - len(new_cards)
    if scheduled:
        print(f"{scheduled} card(s) already scheduled; left in place")

    base = max(other_positions, default=0)
    targets = {card_id: base + step for step, (_, card_id, _) in enumerate(new_cards, start=1)}
    current = {card["cardId"]: card["due"] for card in cards}
    if all(current[card_id] == target for card_id, target in targets.items()):
        print(f"{len(targets)} new card(s) already in source order")
        return

    for card_id, target in targets.items():
        result = invoke("setSpecificValueOfCard", url=url, card=card_id, keys=["due"], newValues=[target])
        if result != [True]:
            raise RuntimeError(f"could not set position of card {card_id}: {result}")
    print(f"Repositioned {len(targets)} new card(s) into source order (positions {base + 1}-{base + len(targets)})")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("markdown_file")
    parser.add_argument("--deck", default="Default")
    parser.add_argument("--tags", nargs="*", default=[])
    parser.add_argument("--url", default=DEFAULT_URL, help="AnkiConnect endpoint (default %(default)s)")
    parser.add_argument("--allow-duplicates", action="store_true",
                        help="add cards even if Anki already has a note with the same front")
    parser.add_argument("--no-reposition", action="store_true",
                        help="leave new-card positions untouched instead of ordering the deck by this file")
    args = parser.parse_args()

    cards = parse_flashcards(args.markdown_file)
    if not cards:
        raise SystemExit(f"No '### Card N' blocks with Front/Back found in {args.markdown_file}")
    print(f"Parsed {len(cards)} cards from {args.markdown_file}")

    version = invoke("version", url=args.url)
    if version < API_VERSION:
        raise SystemExit(f"AnkiConnect API v{version} is too old; need v{API_VERSION}")

    invoke("createDeck", url=args.url, deck=args.deck)  # no-op if the deck already exists
    notes = [make_note(card, args.deck, args.tags, args.allow_duplicates) for card in cards]

    if args.allow_duplicates:
        pairs = list(zip(cards, notes))
    else:
        # Pre-check so one duplicate does not abort the whole batch.
        can_add = invoke("canAddNotes", url=args.url, notes=notes)
        skipped = [card for card, ok in zip(cards, can_add) if not ok]
        pairs = [(card, note) for card, note, ok in zip(cards, notes, can_add) if ok]
        print(f"{len(skipped)} duplicate card(s) skipped, {len(pairs)} to add")
        for card in skipped:
            print(f"  skipped (already exists): {card['front'][:70]}")

    if pairs:
        try:
            note_ids = invoke("addNotes", url=args.url, notes=[note for _, note in pairs])
        except RuntimeError as exc:
            # addNotes rolls back notes added before the failure.
            raise SystemExit(f"addNotes failed, no cards were added: {exc}")

        print(f"Added {len(note_ids)} notes to deck {args.deck!r}")
        for (card, _), note_id in zip(pairs, note_ids):
            print(f"  note {note_id}: {card['front'][:70]}")
    else:
        print("Nothing to add.")

    if not args.no_reposition:
        try:
            reposition_cards(args.deck, [card["front"] for card in cards], args.url)
        except (RuntimeError, SystemExit) as exc:
            print(f"Warning: could not reposition cards: {exc}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
