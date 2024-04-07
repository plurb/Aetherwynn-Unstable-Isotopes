# The Fighter

> *Fighters use their weapons and their physical might to fell their foes.*


<!-- FIXME: re-work to new keywords and templating -->


## Fighter

| Level | Proficiency | Abilities                                  | Fighting Styles | Exploits | Exploit Level |
| ----: | ----------: | :----------------------------------------- | --------------: | -------: | ------------: |
|     1 |           2 | Fighting Style, Exploits, Second Wind (x1) |               1 |        3 |             1 |
|     2 |           2 | Action Surge (x1)                          |               1 |        4 |             1 |
|     3 |           2 | Martial Archetype                          |               2 |        5 |             1 |
|     4 |           2 | Ability Score Increase, Feat               |               2 |        6 |             1 |
|     5 |           3 | Multiattack (2)                            |               3 |        7 |             2 |
|     6 |           3 | Enhanced Strikes                           |               3 |        8 |             2 |
|     7 |           3 | Martial Archetype Ability                  |               3 |        9 |             2 |
|     8 |           3 | Ability Score Increase, Feat               |               3 |       10 |             2 |
|     9 |           4 | Legendary Might (x1)                       |               4 |       11 |             3 |
|    10 |           4 | Martial Archetype Ability                  |               4 |       11 |             3 |
|    11 |           4 | Multiattack (3)                            |               4 |       12 |             3 |
|    12 |           4 | Ability Score Increase, Feat               |               4 |       12 |             3 |

**Note:** Levels beyond 12 aren't ready yet.

---

# Class Abilities

## Hit Points
**Hit Points Per Level:** `10 + your Constitution modifier` per Fighter Level.  
**Hit Dice:** 1d10 per Fighter Level.  

---

## Proficiencies
**Armor:** All Armor, Shields  
**Weapons:** Simple Weapons, Martial Weapons, Firearms  
**Tools:** One set of artisan's tools of your choice  
**Saving Throws:** Strength, Contsitution  
**Skills:** Choose `2 + your Intelligence modifier` of the following: Acrobatics, Athletics, History, Intimidation, Perception, Stealth, and Survival

---

## Equipment
At first level, you start with the following equipment:
* (a) chain mail or (b) leather armor, a longbow, 20 arrows
* (a) martial weapon and shield or (b) two martial weapons
* (a) light crossbow and 20 bolts or (b) two handaxes
* (a) a dungeoneer's pack or (b) an explorer's pack

---

## Multiclassing Into This Class

**Ability Score Requirement:** Strength score or Dexterity score of 13 or greater.  
**Armor Gained:** Light Armor, Medium Armor, Shields  
**Weapons Gained:** Simple Weapons, Martial Weapons  
**Skills Gained:** Choose `1 + half your Intelligence modifier (rounded up)` of the following: Acrobatics, Athletics, History, Intimidation, Perception, Stealth, and Survival  

---

## Fighting Style
*1st-level Ability (Fighter)*  

You learn one Fighting Style from *[Fighter Fighting Styles]*.



You learn additional fighting styles as you gain levels in this class, as shown on the Fighter Table.

---

## Exploits
*1st-level Ability (Fighter)*  

You begin to learn techniques that enhance your martial skill in and out of battle. You gain the following Abilities:

### Stamina

> *You have stamina greater than a mere common soldier, which allows you to perform exploits greater than an ordinary warrior.*

You have a limited well of stamina represented by a number of Stamina Points. You can calculate the number of Stamina Points you have as follows:

**Stamina Points** = `your Fighter Level + your Constitution modifier`

To perform an Exploit, you must expend a number of Stamina Points equal to the Exploit's level. You regain your expended Stamina Points when you finish a *Short Rest* or a *Long Rest*.

For Exploits that modify an *Attack*, *Ability Check*, or *Saving Throw*: you can only use one Exploit per *Attack*, *Ability Check*, or *Saving Throw*.

<!--
NOTE:

> For Exploits that modify an *Attack*, *Ability Check*, or *Saving Throw*:...

This rule is a side effect of SRD 5.6.2 "Timing". It's only here since it's unlikely a new player has read the SRD.
-->

### Exploits Known

You learn `3` Exploits from the [*Fighter Exploit List*](./Fighter%20Exploit%20List.md). The "Exploits" column of the Fighter Table shows when you learn more Exploits of your choice. To learn a Exploit, you must be able to learn Exploits of its level, as well as meet any other prerequisites (listed under **Pre-requisites** in the Exploit's entry).

Whenever you gain a Fighter Level, you can replace one of the Exploits you learnt from this class with another Exploit from the *Fighter Exploit List*.

### Saving Throws

If one of your Exploits requires a creature to make a saving throw, your Exploit DC is calculated as follows:

**Exploit Save DC** = `8 + your Proficiency Bonus + your Strength or Dexterity modifier (your choice)`

---

## Second Wind
*1st-level Ability (Fighter)*  

> *You draw a long and weary breath, steeling your resolve and pushing forwards.*

🔵 **(1/short rest)** — You regain `1d10 + X` hp, where `X = your Fighter level`.

If you have no remaining uses of "Second Wind", you can expend `2` *Stamina Points* to use it again.

At 14th level in this class, you can use "Second Wind" **2/short rest** without expending *Stamina Points*.

---

## Action Surge
*2nd-level Ability (Fighter)*  

> *You can momentarily push yourself beyond human limits.*

◻️ **(1/short rest, 1/turn)** — You may take 1 additional Major Action this turn. This Action cannot be used to cast a spell.

At 18th level in this class, you can use "Action Surge" **2/short rest**.

---

## Martial Archetype
*3rd-level Ability (Fighter)*

> *You have distinguished yourself from the common warrior, and have gained skills that represent your unique skillset.*

Choose one of the following Martial Archetypes:

| Martial Archetype | Source                  |
| :---------------- | :---------------------- |
| Arcane Knight     | Unstable Isotopes (0.0) |
| Battle Master     | Unstable Isotopes (0.0) |
| Bodyguard         | Unstable Isotopes (0.0) |
| Cataphract        | Unstable Isotopes (0.0) |
| Champion          | Unstable Isotopes (0.0) |
| Commander         | Unstable Isotopes (0.0) |
| Guerilla          | Unstable Isotopes (0.0) |
| Legionaire        | Unstable Isotopes (0.0) |
| Marksman          | Unstable Isotopes (0.0) |

### Archetype Exploits

Each Archetype has a list of Exploits you learn at the Fighter levels noted in the Archetype's description. They do not count against the total number of Exploits you know and cannot be switched out for other Exploits. If you do not meet an Archetype Exploit's pre-requisites, you learn it anyways.

---

## Ability Score Increase
*4th-level Ability (All Classes)*

Increase one Ability Score of your choice by 2, or you increase two Ability Scores of your choice by 1. You cannot increase an Ability Score above 20 using this Ability.

You can do so again at 8th, 12th, 14th, 16th, and 19th level in this class.

---

## Feat
*4th-level Ability (All Classes)*

You earn a Feat. This Feat can be either a *General*, *Martial*, or *Fighter* Feat. You earn additional Feats at 8th, and 12th level in this class.

---

## Multiattack
*5th-level Ability (Barbarian, Fighter, Monk)*  

> *You can strike with inhuman speed.*

♾️ — You Attack up to `2` times, instead of once, when you take the *Attack* Action on your turn.

The number of attacks you can make when you take the *Attack Action* increases; at 11th level (3 attacks total) and at 17th level (4 attacks total) in this class.

---

## Enhanced Strikes
*6th-level Ability (Barbarian, Fighter, Monk, Rogue)*  

♾️ — *Weapon Attacks* you make count as *Magical* for the purpose of overcoming *Resistance* and *Immunity* to Non-*Magical* *Attacks* and Damage.

---

## Legendary Might
*9th-level Ability (Fighter)*  

◻️ **(1/long rest, triggered)** — If you fail a *Saving Throw*, you may succeed instead.

You can use "Legendary Might" **2/long rest** starting at 13th level, and **3/long rest** starting at 17th level in this class.

<!-- References -->

<!-- External references. -->
[Fighter Fighting Styles]: ./Fighter%20Fighting%20Styles.md

<!---------------->
