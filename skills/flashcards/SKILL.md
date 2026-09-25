---
name: flashcards
description: Turn source material into high-quality Anki flashcards and push them into Anki. Use when asked to make flashcards or study cards from an article, docs, or notes, to push existing flashcard markdown into Anki, or to add cards to Anki for spaced repetition.
---

# Flashcards

A flashcard earns its review time by forcing **active recall** of one atomic fact. Build cards that stay gradeable for months, then push them into Anki through the bundled script.

## Workflow

1. Harvest the source. Read it whole before writing a card. Collect what a practitioner must have available under pressure — definitions, mechanisms, contrasts, numbers, failure modes — and cover the source's core ideas rather than one card per sentence.
2. Design each card against [reference.md](reference.md). Every card carries one atomic fact, a prompt that forces recall, enough context to stand alone, and exactly one gradeable answer. Split any card whose answer holds two facts.
3. Write the deck file in the format the pusher parses:

   ```markdown
   ### Card 1
   **Front:** What does DNS translate?
   **Back:** Domain names into IP addresses.
   ```

   One `### Card N` heading per card, single-line Front and Back. Name it `<topic>-flashcards.md` and save it where the repo keeps notes, or next to the source. When the user brings an existing file in this format, start at step 4.
4. Push to Anki with the bundled script (relative to this skill's folder), run while Anki is open:

   ```bash
   python3 scripts/anki_add_cards.py <file.md> --deck "<Topic>" --tags <tag>...
   ```

   The script creates the deck, skips fronts that already exist anywhere in the collection and names each skip, and is safe to re-run. It also orders the deck's new cards to follow this file, so the source's sequence becomes the study sequence; cards from other files stay ahead, and already-scheduled cards keep their scheduling. Pass `--no-reposition` to leave positions alone. If AnkiConnect does not answer, open Anki; if it still does not, install the add-on (Tools → Add-ons → Get Add-ons… → code `2055492159`) and restart Anki.
5. Verify and report. Re-run the script: every card must come back as a skipped duplicate, none added, and the new cards already in source order. Report the deck, the notes added, any duplicates that already existed, and the final order.

## Reference

Read it at step 2:

- **[reference.md](reference.md)** — what earns a card, the formulation rules, the formatting contract, and the ship checklist.

## Gotchas

- Anki must be running: AnkiConnect lives inside Anki and dies with it.
- Keep one AnkiConnect add-on folder; two copies fight over port 8765.
- AnkiConnect has no authentication and listens on localhost only. Keep it that way.
- The duplicate check compares the front text as stored, so re-run the pusher rather than editing cards by hand; `--allow-duplicates` adds copies deliberately.

## Completion

The work is complete when:

- Every card passes the [reference.md](reference.md) checklist and covers a core idea of the source.
- The deck file and the Anki collection hold the same cards: each one added, or reported as an existing duplicate with its location.
- The deck's new cards follow the file's order, and the final script run reports zero additions with every card already in source order.
