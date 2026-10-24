# Copyright Cnosu System 2026. GPLv3 license, see the LICENSE.md file.

CSI = "\033["


def code_to_chars(code: int) -> str:
    # Adds the CSI escape code along with an m to the integer
    return f"{CSI}{code}m"


class AnsiCodes:
    # Formats integers into working codes, if not an integer, skips it
    def __init__(self):
        for name, value in vars(type(self)).items():
            if not name.startswith("_") and isinstance(value, int):
                setattr(self, name, code_to_chars(value))


class AnsiFore(AnsiCodes):
    # Standard colors
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37

    # Not standard but fairly supported colors (B stands for Bright)
    B_BLACK = 90
    GRAY = 90
    B_RED = 91
    B_GREEN = 92
    B_YELLOW = 93
    B_BLUE = 94
    B_MAGENTA = 95
    B_CYAN = 96
    B_WHITE = 97

    # Handle the 256 Colors format
    def Color(self, id: int) -> str:
        if not isinstance(id, int) or not 0 <= id <= 255:
            raise ValueError("Color ID must be an integer from 0 to 255")
        return f"{CSI}38;5;{id}m"

    # Handle the RGB format
    def RGB(self, r: int, g: int, b: int) -> str:
        if not all(type(c) is int and 0 <= c <= 255 for c in (r, g, b)):
            raise ValueError("RGB values must be integers from 0 to 255")
        return f"{CSI}38;2;{r};{g};{b}m"


class AnsiBack(AnsiCodes):
    # Standard colors
    BLACK = 40
    RED = 41
    GREEN = 42
    YELLOW = 43
    BLUE = 44
    MAGENTA = 45
    CYAN = 46
    WHITE = 47

    # Not standard but fairly supported colors
    B_BLACK = 100
    GRAY = 100
    B_RED = 101
    B_GREEN = 102
    B_YELLOW = 103
    B_BLUE = 104
    B_MAGENTA = 105
    B_CYAN = 106
    B_WHITE = 107

    # Handle the 256 Colors format
    @staticmethod
    def Color(id: int) -> str:
        if type(id) is not int or not 0 <= id <= 255:
            raise ValueError("Color ID must be an integer from 0 to 255")
        return f"{CSI}48;5;{id}m"

    # Handle the RGB format
    @staticmethod
    def RGB(r: int, g: int, b: int) -> str:
        if not all(type(c) is int and 0 <= c <= 255 for c in (r, g, b)):
            raise ValueError("RGB values must be integers from 0 to 255")
        return f"{CSI}48;2;{r};{g};{b}m"


class AnsiStyle(AnsiCodes):
    # Codes for different styles
    BRIGHT = 1
    BOLD = 1
    DIM = 2
    ITALIC = 3
    UNDERLINE = 4
    BLINK = 5
    R_BLINK = 6
    REVERSE = 7
    STRIKETHROUGH = 9


class AnsiReset(AnsiCodes):
    # Codes for resetting
    FORE = 39
    BACK = 49
    ALL = 0


Fore = AnsiFore()
Back = AnsiBack()
Style = AnsiStyle()
Reset = AnsiReset()
