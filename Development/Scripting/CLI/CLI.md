# Aetherwynn CLI

CLI specification.

Aetherwynn CLI:
* base command shall be `aether`

## `aether [search|get|GET]`

`aether [search|get|GET] [-name] [name]` - fetches the **first** document or feature w/ the specified name (nearest match)
* `-name` - the item to search for (optional, useful when using multiple flags/arguments)
* `-rule` - limits search to rules.
  * `-rule condition` - limits search to conditions.
  * `-rule spellcasting` - limits search to rules for spellcasting.
  * `-rule exploits` - limits search to rules for exploits.
* `-exploit` - limits search to exploits.
  * `-exploit "classes=[class 1] [class 2] [class 3]..."` - searches through the specified class(es)'s exploit lists.
  * `-exploit "level = [level]"` - searches for spells of the specified level.
  * `-exploit "level<=[level]"` - searches for spells where `exploitLevel <= level`.
  * `-exploit "[lower] <= level <= [upper]"` - searches for spells where `lower <= exploitLevel <= upper`
  * `-exploit "[lower] < level < [upper]"`
  * `-exploit "level > [level]"`
  * `-exploit "level >= [level]"`
* `-spell` - limits search to spells.
  * `-spell "classes=[class 1] [class 2] [class 3]..."` - searches through the specified class(es)'s spell lists.
  * `-spell "level = [level]"` - searches for spells of the specified level.
  * `-spell "level<=[level]"` - searches for spells where `spellLevel <= level`.
  * `-spell "[lower] <= level <= [upper]"` - searches for spells where `lower <= spellLevel <= upper`
  * `-spell "[lower] < level < [upper]"`
  * `-spell "level > [level]"`
  * `-spell "level >= [level]"`
  * `-spell "school=[school 1] [school 2] [schoo 3]..."` - searches for the specified spell school(s).
  * The above commands can be combined.
* `-classfeat` - limits search to class features.
  * `-classfeat [class name]` - limits search to features of a particular class
  * `-classfeat channel-divinity` - limits search to channel divinities.
    * `-classfeat [class name] channel-divinity` - limits search to channel divinites of a particular class.
  * `-classfeat channel-elements` - limits search to channel elements.
  * `-classfeat eldritch-invocations` - limits search to eldritch invocations.
  * `-classfeat fighting-styles` - limtis search to fighting sytles.
    * `-classfeat [class name] fighting-styles` - limits search to fighting styles of a particular class.
* `-feat` - limits search to feats.
  * `-feat general` - limits search to general feats.
  * `-feat lineage` - limits search to lineage feats.
  * `-feat [class name]` - limits search to feats belonging to the specified class.
  * `-feat [subclass name]` - limits search to feats belonging to the specified subclass.
  * `-feat spellcasting` - limtis search to spellcasting feats.
  * `-feat martial` - limits search to martial feats.
  * `-feat metamagic` - limits search to metamagic options.
  * `-feat channel-divinity` - limits search to channel divinity feats.
  * `-feat channel-elements` - limits search to channel elements feats.
  * `-feat eldritch-invocations` - limits search to eldritch invocation feats.
* `-item` - limits search to items.
  * `-item "tags=[tag 1] [tag 2] [tag 3]..."` - searches by item tags.
  * `-item bonus=[+1|+2|+3]` - limits search to items with the specified bonus.
    * Supports comparison syntax.
  * `-item genericvariant=[false|true]` - whether to allow generic variants to appear in the search.
  * `-item specificvariant=[false|true]` - whether to allow specific instances of variants to appear.
  * `-item "rarity=[common|uncommon|rare|very rare|legendary|artifact|None]"` - searches by item rarity.
    * Supports comparison syntax.
* `--echo` - displays the search routes as it searches.
* `--noprogress` - disables the progress bar.
* `--regex` - searches for the document w/ the specified name using regex matching.
* `--fetchall` - gets **all** matches, not just the first one.
* `--nocache` - disables search result caching for this search (this options does nothing it `-remote` is used).
* `-remote=[url]` - uses remote server for the fetch.
* `-[o|out|output] [filename]` - puts the search result into the specified file. if the file doesn't exist, it creates a new one.
* `-[reqfile|req|f]` - file containing search flags in JSON format (or SQL format if `-sql` is used).
* `--sql` - search using SQL syntax. Only works when using the `-[reqfile|req|f]` flag.


## `aether newchar`
<!-- TODO: Fix to use Avrae/DiceCloud V2 as DiceBox is an abandoned project -->
`aether newchar` - creates new empty character sheet (default is DiceBox)
* `--dicebox` - (default) creates the new character in DiceBox format.
* `--pdf` - creates a fillable PDF.


## `aether loadchar`

`aether loadchar [path|URL]` - loads character for aetherwynn automations (default format is DiceBox)
* `--dicebox` - (default) loads a DiceBox character.
* `--dicecloud` - loads a Dicecloud v2 character, requires URL to the sheet.
* `--dicecloudv1` - loads a Dicecloud v1 character, gives the following warning when used:
  * `WARNING: Dicecloud v1 is at EOL, and is out of date. Use Dicecloud v2 or DiceBox instead geezer.`
  * FUTURE: After DiceBox development is complete, deprecate this feature. Then remove in the next stable release.
* `--tableplop` - loads a tableplop sheet.
* `--critterdb` - loads a CritterDB monster.



