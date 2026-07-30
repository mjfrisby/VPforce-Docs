# Instructions for Documentation Project

This file provides guidance for agents when writing, editing, and improving technical documentation in this MkDocs project.

## Language and Style

- Use Orwell Writing guidelines
- Use **concise, clear, and factual language**
- Avoid unnecessary filler words, marketing tone, or repetition
- Prefer **active voice** over passive voice
- Keep sentences **short and direct** (aim for 15-20 words per sentence)
- Write in a **professional, direct, and reader-focused** tone


## Markdown Formatting

Follow correct Markdown syntax at all times. Prefer MkDocs-compatible styling and the repository's existing conventions.

- Use proper heading hierarchy (`#`, `##`, `###`, etc.)
- Format code blocks with appropriate language tags (for example: ```python or ```bash)
- Create valid links: `[link text](URL)` or `[link text](relative/path.md)`
- Use consistent list formatting (either `-` or `*` for unordered lists, `1.` for ordered)
- Format inline code with single backticks: `` `code` ``
- Use tables correctly with proper alignment

Important formatting notes:

!!! note "Blank line before lists"

	When creating a list, include a blank line before the list block. This ensures correct rendering across MkDocs themes and avoids incorrect nesting in some renderers.

!!! note "Sublist formatting"

	For nested lists (sublists), use proper indentation:
	- Indent sublists with **4 spaces** (not 2)
	- Add a **new empty line after the parent item** before starting the sublist
	- This ensures correct rendering of nested list structures in MkDocs

!!! note "Admonitions"

	Use MkDocs-style admonitions for inline guidance instead of plain bold/italic labels. Examples:

	- `!!! note "Note"` for informational notes
	- `!!! tip "Tip"` for helpful hints
	- `!!! warning "Warning"` for cautions
	- `!!! important "Important"` for critical points

	Admonitions should be used for notes, warnings, important caveats, or any UI/behavioral exceptions that readers must see.

!!! note "Line Breaks"

	To create a line break within a paragraph, add **two spaces** at the end of the line. This ensures consistent rendering across different Markdown parsers.

## Terminology and Consistency

- Maintain **consistent terminology** throughout all documentation
- Use standard **units and measurements** consistently
- Follow the existing **style conventions** in the project
- Preserve capitalization patterns (e.g., product names, technical terms)
- Keep acronyms consistent (define on first use, then use abbreviated form)

## Code Examples

All code examples should be:

- **Correct and tested** (or clearly marked as pseudocode)
- **Minimal** - include only what's necessary to demonstrate the concept
- **Well-commented** when complexity requires explanation
- **Properly formatted** with appropriate syntax highlighting
- **Relevant** to the surrounding documentation context

## Document Structure

When editing existing documents:

- **Preserve the existing structure** (headings, sections, flow)
- Maintain the established organization and hierarchy
- Don't reorganize content unless explicitly requested
- Keep related information grouped together
- Respect existing navigation patterns and cross-references

## Handling Uncertainty

If uncertain about a technical fact or detail:

- **Flag it** with a comment like `<!-- TODO: Verify this detail -->`
- Use qualifying language ("typically", "generally", "may")
- Suggest verification rather than stating as absolute fact
- Do not fabricate technical specifications or requirements

## Documentation Conventions

- **Respect all existing conventions** in this project
- Do not introduce stylistic drift or inconsistencies
- Follow the patterns established in existing documentation
- Match the tone and formality level of surrounding content
- Preserve any project-specific formatting or notation systems

## FAQ Formatting

When creating FAQ sections, use the following format for consistency and readability:

```markdown
## FAQ

**Q: Question text here?**  
**A:** Answer text here.

**Q: Another question?**  
**A:** Another answer.
```

Key points:

- Use `## FAQ` as the section heading
- Format questions with `**Q:**` prefix
- Format answers with `**A:**` prefix
- Add two spaces at the end of the Q line (before the line break) to ensure proper separation
- Each Q&A pair should be separated by a blank line for better readability
- Keep both Q and A on separate lines for consistency

## Changelog Management

When documentation changes are made, maintain `changelog.md` (or the appropriate date-versioned changelog) to record user-facing changes:

### What to Document in Changelog

Document **additions and improvements to user-facing documentation only**. Focus on:

- New sections or pages added
- Major content enhancements or clarifications
- New features or capabilities documented
- Improvements to existing explanations or procedures
- Troubleshooting guidance additions

**Do NOT document** project infrastructure, internal processes, or technical implementation details.

### Changelog Format

Use this simple list format with dates:

```markdown
- **Date:** 2025-10-10

    - Change description 1
    - Change description 2
    - Change description 3
```

Each changelog entry should be a concise bullet point describing what was added or improved. Maintain formatting structure for sublists.

### Language for Changelog

- Use **user-focused language** - explain benefits and capabilities, not internal changes
- Write from the **reader's perspective** - what can they now do?
- Keep entries **concise** - One clear sentence per bullet point
- Use **active voice** - "Added...", "Documented...", "Expanded..." rather than passive voice

### Linking to New Sections

When documenting new sections or pages added, include cross-references using this format:

```markdown
- Added new section **[Section Name][section-slugged]** explaining...
```

MkDocs will automatically create links to relevant pages. Use slug format for section links:
- Convert heading text to lowercase
- Replace spaces with hyphens
- Remove special characters (keep only alphanumeric and hyphens)

Example: "Understanding Native DCS FFB" becomes `understanding-native-dcs-ffb`

---

**Remember:** Your role is to enhance clarity and accuracy while maintaining consistency with the existing documentation standards. When in doubt, preserve what's already there rather than introducing changes.

-----

# Orwell Writing

## Overview

Use Orwell's rules and ASD-STE100 Simplified Technical English (STE) as practical filters for clear, direct, and honest prose. Use STE by default for technical, instructional, business, and product prose. Apply the rules to both drafting and revision, but do not erase deliberate voice, character, rhythm, humor, or genre when the user clearly wants them.

STE has writing rules and a controlled dictionary. Use an approved word with its approved meaning when the dictionary is available. Do not claim strict STE conformance without checking the current ASD-STE100 issue and dictionary.

## Core Rules

Remember these rules from "Politics and the English Language":

1. Never use a metaphor, simile, or other figure of speech which you are used to seeing in print.
2. Never use a long word where a short one will do.
3. If it is possible to cut a word out, always cut it out.
4. Never use the passive where you can use the active.
5. Never use a foreign phrase, a scientific word, or a jargon word if you can think of an everyday English equivalent.
6. Break any of these rules sooner than say anything outright barbarous.

## ASD-STE100 baseline

For technical and instructional prose:

1. Use short sentences. Put one main action or statement in each sentence.
2. Use a clear subject and an active verb. Name the actor when the actor matters.
3. Use the same term for the same thing. Do not change a term only to avoid repetition.
4. Use familiar words with one precise meaning. Avoid idioms, slang, figurative language, and vague verbs.
5. Use a specific technical term when it is necessary for accuracy. Define it or link to its definition.
6. Keep noun groups short. Use prepositions to show relationships between terms.
7. Write procedures as direct instructions. State the condition, action, and expected result.
8. Use positive instructions when they are clear. State what the reader must do.
9. Use consistent American English spelling unless the user's style guide requires another variety.
10. Preserve code, commands, identifiers, product names, legal text, and required quotations. Do not simplify them silently.

When strict STE is not possible, keep the text clear and mark the terms or passages that need a domain-specific exception.

## Workflow

When writing from scratch:

1. Identify the audience, purpose, and promised tone from the user's request.
2. Draft in concrete, direct English.
3. Remove stock phrases, dead metaphors, filler, pompous diction, needless abstraction, and avoidable jargon.
4. Prefer active verbs and clear subjects unless passive voice better serves emphasis, tact, suspense, or technical accuracy.
5. Keep necessary nuance; do not make prose crude, false, or flat just to make it short.
6. Apply the ASD-STE100 baseline. Check terms, sentence structure, instructions, and technical exceptions.

When revising existing text:

1. Preserve the user's meaning and any explicit tone or format constraints.
2. Cut words, clauses, and sentences that do no work.
3. Replace stale figures of speech with plain phrasing or a fresh, specific image.
4. Replace long, foreign, scientific, or jargon terms with everyday English when accuracy permits.
5. Convert passive constructions to active ones when the actor matters and is known.
6. Flag any remaining jargon, passive voice, or ornate phrasing that is necessary rather than silently removing important precision.
7. Run a final STE pass. Check that each technical term is consistent, each instruction states the required action, and each exception is intentional.

## Creative Writing

For fiction, poetry, memoir, scripts, and lyrical prose, treat STE as a clarity aid, not a requirement that overrides the user's form. Keep intentional ambiguity, cadence, dialogue style, imagery, and character voice when they create a real effect. Remove only language that feels inherited, inflated, evasive, or lazy. Use strict STE when the user explicitly requests it, and note when that request conflicts with a creative effect.

