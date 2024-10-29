# Aetherwynn Style Guide

This is the style guide for the Aetherwynn TTRPG. This document outlines the visual and grammatical style of all documents within the game. Any pull request to this repository **must** conform with this guide before it can be approved. The style guide does not apply to the style guide itself.

---

## Language & Spelling

This repository is meant for an international, English-speaking audience. Thus, *all* text within documents should use the English (UK) spellings of words. Regional dialects of English, slang, and non-English will face some scrutiny. English (US) spellings are strictly prohibited.

Remember to put your code through a spell checker before committing/submitting a pull request.

### Add These To Your Spellchecker's Dictionary

* Aetherwynn
* Multiclass
* Multiclassing
* Pyromancy
* Spellcasting
* TTRPG
* ... More to come...

---

## Never Hard Wrap

Markdown text must never "Hard Wrap" paragraphs. This means that paragraph text must all be on a single line.

Some examples:

```md
**INCORRECT**

This is a 
hard wrapped paragraph.
```

Note how a newline is placed abruptly in the middle of the sentence.

```md
**INCORRECT**

This is a longer.
Hard wrapped paragraph.
```

Each sentence is placed on a new line forcibly.

```md
**CORRECT**

This is a long sentence. It all continues on a single line.
```

By keeping the paragraph on a single line, it prevents hard stops while reading source text. In order to display long lines like these properly when editing, it's recommended to enable **Soft Line Wrapping** in your text editor of choice.

---

## Headings

Follow the linter settings for headings. This means:
* Use ATX-style headings (hashtags).
* Increment headings by one level only.
* No duplicate headings.
* Do not end headings with punctuation.

Example:

```md
**INCORRECT**

# I Am A Naughty Nelly

Blah blah blah...

### I Incremented The Headings Wrong!!!

```

```md
**CORRECT**

# A Proper Title

Some text...

---

## I Am A Sane Individual

More text...

---
```

---

## Tags

Tags always go immediately under the heading of the ability/item/class it seeks to tag. There is more information about tags in the [wording guide][WG].

Example:

```md
**INCORRECT**

### An Ability Name

*(Tags...)*

---

### Another Ability Name *(Tags...)*

---
```

```md
**CORRECT**

### An Ability Name
*(Tags...)*

---

### Another Ability Name
*(Tags...)*

---
```

---

## Flavour Text

"Flavour text" is text that has no real game effects. Flavour text is generally descriptive text. The text should be *italicized* and put in a block quote.

An example:

```md
**INCORRECT**

### Fireball
*3rd-level Spell (Evocation)*  
**Costs:** `3` "Mana"  
**Empower:** `1` "Mana" per "Spell Level"  
**Casting Time:** 🔷🔷  
**Range:** 120 ft.  
**Components:** V, S  
**Duration:** Instantaneous  

You shoot a streak of flame from your fingertip, which blooms into a a large plume of flame.

Make a *Ranged Spell Attack* vs. *Reflex* against creatures and objects in a 20 ft. sphere centred on target point in range.

...
```

```md
**CORRECT**

### Fireball
*3rd-level Spell (Evocation)*  
**Costs:** `3` "Mana"  
**Empower:** `1` "Mana" per "Spell Level"  
**Casting Time:** 🔷🔷  
**Range:** 120 ft.  
**Components:** V, S  
**Duration:** Instantaneous  

> *You shoot a streak of flame from your fingertip, which blooms into a large plume of flame.*

Make a *Ranged Spell Attack* vs. *Reflex* against creatures and objects in a 20 ft. sphere centred on target point in range.

...
```

---

## Rules Text

Rules text is paragraph text. Rules text always goes *after* flavour-text.

---

## Referring to The Reader

In general, rules text serve as instructions for the player or GM to execute. When referring to the reader in rules-text, always refer to them in **second person.**

---

## Dice

Whenever dice need to be rolled, the dice should be kept in `inline code`. (e.g. `2d6`, `1d20`).

> [!IMPORTANT]
>
> A singular die is a "die", the plural form is "dice". You roll a single *die*. You roll multiple *dice*.

Example:

```md
**INCORRECT**

### Fireball (Simplified)
*3rd-level Spell (Evocation)*  
**Costs:** `3` "Mana"  
**Empower:** `1` "Mana" per "Spell Level"  
**Casting Time:** 🔷🔷  
**Range:** 120 ft.  
**Components:** V, S  
**Duration:** Instantaneous  

You shoot a streak of flame from your fingertip, which blooms into a a large plume of flame.

Make a *Ranged Spell Attack* vs. *Reflex* against creatures and objects in a 20 ft. sphere centred on target point in range.

**Success:** It takes 6d6 fire Damage.  
**Failure:** It takes half as much Damage.  

...
```

```md
**CORRECT**

### Fireball (Simplified)
*3rd-level Spell (Evocation)*  
**Costs:** `3` "Mana"  
**Empower:** `1` "Mana" per "Spell Level"  
**Casting Time:** 🔷🔷  
**Range:** 120 ft.  
**Components:** V, S  
**Duration:** Instantaneous  

> *You shoot a streak of flame from your fingertip, which blooms into a large plume of flame.*

Make a *Ranged Spell Attack* vs. *Reflex* against creatures and objects in a 20 ft. sphere centred on target point in range.

**Success:** It takes `6d6 [fire]` Damage.
**Failure:** It takes half as much Damage.  
```

---

## Keywords

Keywords are global definitions that have very specific usages see the [wording guide][WG] for more information on keywords. Keywords are *italicized*.

---

## References

References are references to abilities, classes, tags, attributes, or any non-global entry. For more information, see the [wording guide][WG]. References are put inside "quotation marks".

---

## Soft-Keywords

Soft keywords are keywords that are either undefined, weakly defined, or cannot be defined. See the [wording guide][WG] for more info. Soft keywords are written as regular paragraph text, or put inside "quotation marks".

---

## X Formatting

X formatting refers to using `X` to specify some unknown quantity in formulas. `X` is always put in `inline code`, and the method to derive `X` is put in a "where `X = ...`" section in a section after `X` stops being used. `X` is always *added* to constants. Constants are *subtracted* from `X`.

Example:

```md
**INCORRECT**

### Fireball
*3rd-level Spell (Evocation)*  
**Costs:** `3` "Mana"  
**Empower:** `1` "Mana" per "Spell Level"  
**Casting Time:** 🔷🔷  
**Range:** 120 ft.  
**Components:** V, S  
**Duration:** Instantaneous  

> *You shoot a streak of flame from your fingertip, which blooms into a large plume of flame.*

Make a *Ranged Spell Attack* vs. *Reflex* against creatures and objects in a 20 ft. sphere centred on target point in range.

**Success:** It takes `Xd6 [fire]` where `X = this Spell's level + 3` Damage.
**Failure:** It takes half as much Damage. 
```

```md
**CORRECT**

### Fireball
*3rd-level Spell (Evocation)*  
**Costs:** `3` "Mana"  
**Empower:** `1` "Mana" per "Spell Level"  
**Casting Time:** 🔷🔷  
**Range:** 120 ft.  
**Components:** V, S  
**Duration:** Instantaneous  

> *You shoot a streak of flame from your fingertip, which blooms into a large plume of flame.*

Make a *Ranged Spell Attack* vs. *Reflex* against creatures and objects in a 20 ft. sphere centred on target point in range.

**Success:** It takes `Xd6 [fire]` Damage, where `X = 3 + this Spell's level`.
**Failure:** It takes half as much Damage.  
```

---

## Horizontal Rule Style

When placing horizontal rules in your documents, always use three dashes (`---`) over any other method.

An example:

```md
**INCORRECT**

A paragraph

===

Another paragraph.
```

```md
**CORRECT**

A paragraph

---

Another paragraph.
```

Always place horizontal rules between sections in your documents.

Another example:

```md
# A Big Heading

> *Flavour text...*

Some rules text...

---

## A Smaller Heading

> *More flavour text...*

More rules text...

---
```

Always place a horizontal rule at the end of each file. See the above example.

---

## Links

Links must follow the markdown linter's settings. Place the endpoints of links at the *end* of the file, past the final horizontal rule.

```md
# A Big Heading

> *Flavour text...*

Some rules text... A [link][L1]!

---

## A Smaller Heading

> *More flavour text...*

More rules text...

---
[L1]: ./Style%20Guide.md
```

**DO NOT USE FOOTNOTES.**

---

[WG]: ./Wording%20Guide.md
