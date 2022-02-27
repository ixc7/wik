import random

X = '\x1b['

BOLD = f'{X}1m'
UNDERLINE = f'{X}4m'
END = f'{X}0m'

PURPLE = f'{X}95m'
CYAN = f'{X}96m'
DARKCYAN = f'{X}36m'
BLUE = f'{X}94m'
GREEN = f'{X}92m'
YELLOW = f'{X}93m'
RED = f'{X}91m'
ALL = [PURPLE, CYAN, DARKCYAN, BLUE, GREEN, YELLOW, RED]

def randomColor():
    return ALL[random.randrange(len(ALL)-1)]
