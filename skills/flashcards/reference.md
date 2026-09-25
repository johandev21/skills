# Reference — Card design

Reference for workflow step 2. A card is a retrieval unit: the prompt forces recall, the answer is what comes back. Every rule below serves that one behaviour.

## What earns a card

Card what a practitioner must have available under pressure: definitions, mechanisms, contrasts, numbers, failure modes, rules of thumb. Leave out anything that can be looked up in seconds and never needs to be recalled — a deck of trivia dilutes the facts that matter.

## Formulation rules

- **One fact per card.** If the answer carries two independently testable facts, split the card. Atomic cards fail small and grade fast.
- **Prompt recall, not recognition.** Phrase the front as a direct question; yes/no and multiple-choice prompts only test recognition.
- **Make it standalone.** Cards are reviewed out of order, months later. Name the subject inside the prompt ("In TCP, …") and drop source-relative references ("as shown above").
- **Exactly one gradeable answer.** A knowledgeable reader must judge right or wrong instantly. "List everything about X" cannot be graded; split it.
- **Short, plain words.** Write the answer the way you would say it in an interview. Front and Back stay on one line each.
- **Your words, not the source's.** Restating an idea tests understanding; copying a sentence tests the sentence.
- **Understand first.** Card material you can already explain. Cards maintain knowledge; they do not create it.
- **Concrete over abstract.** Anchor a rule in the example that shows it, where one exists.
- **Watch interference.** Sibling cards with near-identical prompts or answers get confused with each other. Merge them or sharpen the context that tells them apart.
- **Give lists a hook.** Sets resist recall: give each item its own card, or attach a mnemonic or ordering hook to the answer.
- **Extract embedded facts.** When a fact lives inside a sentence — a number, an order, a name — pull it into a direct question instead of carding the whole sentence.

## Formatting

Card text renders inline markdown: `code` becomes code-styled and **bold** becomes bold; everything else shows literally. Use them for identifiers and key terms, not decoration.

## Checklist

Ship a card only when every answer is yes:

- Does the front force recall of exactly one fact?
- Can it be answered without the source, months from now?
- Is there exactly one correct answer, gradeable at a glance?
- Would a practitioner say it this way?
- Does any sibling card make it guessable or confusable?
