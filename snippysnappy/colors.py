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
    Black = 30
    Red = 31
    Green = 32
    Yellow = 33
    Blue = 34
    Magenta = 35
    Cyan = 36
    White = 37

    # Not standard but fairly supported colors (B stands for Bright)
    B_Black = 90
    Gray = 90
    B_Red = 91
    B_Green = 92
    B_Yellow = 93
    B_Blue = 94
    B_Magenta = 95
    B_Cyan = 96
    B_White = 97

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
    Black = 40
    Red = 41
    Green = 42
    Yellow = 43
    Blue = 44
    Magenta = 45
    Cyan = 46
    White = 47

    # Not standard but fairly supported colors
    B_Black = 100
    Gray = 100
    B_Red = 101
    B_Green = 102
    B_Yellow = 103
    B_Blue = 104
    B_Magenta = 105
    B_Cyan = 106
    B_White = 107

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
    Bright = 1
    Bold = 1
    Dim = 2
    Italic = 3
    Underline = 4
    Blink = 5
    Reverse = 7
    Strikethrough = 9


class AnsiReset(AnsiCodes):
    # Codes for resetting
    Fore = 39
    Back = 49
    All = 0


Fore = AnsiFore()
Back = AnsiBack()
Style = AnsiStyle()
Reset = AnsiReset()
