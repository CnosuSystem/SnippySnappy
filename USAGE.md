# USAGE


## colors.py

A simple interface for generating ANSI escape sequences to format terminal output. It supports:
* Standard foreground and background colors.
* Bright foreground and background colors (not standard but fairly supported).
* 256 Colors palette (you can see [this](https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit) Wkipedia article for a lookup table).
* 24-bit RGB colors.
* Text styles such as bold, italic, underline, and strikethrough.
* Resetting foreground colors, background colors, and all formatting.

The module exposes four pre-initialized objects:

| Object | Description            |
| ------ | ---------------------- |
| Fore   | Foreground text colors |
| Back   | Background colors      |
| Style  | Text formatting styles |
| Reset  | Formatting reset codes |

These objects return ANSI escape sequences as strings. Insert them into your output to apply formatting in terminals that support ANSI codes. Example usage:

```python
from snippysnappy import Fore, Back, Style, Reset

print(f"{Fore.RED}This text is red.{Reset.ALL}")
print(f"{Back.BLUE}This text has a blue background.{Reset.ALL}")
print(f"{Style.BOLD}This text is bold.{Reset.ALL}")
```


## ids.py

Functions and their usage:

`get_id(string: str, len: int)`
Returns a SHA256 of the given string. Use the len argument to cut the length of the given hash.
  * string - text to get hashed
  * len - how many characters of this hash should get returned (set 0 for the whole one)
Example usage:

```python
import snippysnappy

name = "Obelius"
id = snippysnappy.get_id(name, 8)

print(f'Connecting to "{id}: {name}"...')
```