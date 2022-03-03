class colors:
    black_bg = "\033[40m"
    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    white = "\033[37m"
    grey = "\033[90m"
    bright_red = "\033[91m"
    bright_green = "\033[92m"
    bright_yellow = "\033[93m"
    bright_blue = "\033[94m"
    bright_magenta = "\033[95m"
    bright_cyan = "\033[96m"
    bright_white = "\033[97m"
    end = "\u001b[0m"
    endl = "\u001b[0m\n"
    underline = "\033[4m"
    italic = "\033[3m"
    bold = "\u001b[1m"


def clear():
    import os

    os.system("clear||cls")
    print_header()


def cprint(color=colors.blue, s="", end=colors.endl):
    print(color + s, end=end)


def print_header():
    cprint(colors.magenta, "-$-$-$- Blackjack 1000 -$-$-$-")
    return ""
