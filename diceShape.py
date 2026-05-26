import enum

class DiceShape(enum.Enum):
    dfour = ["d4", 4]
    dsix = ["d6", 6]
    deight = ["d8", 8]
    dten = ["d10", 10]
    dtwelve = ["d12", 12]
    dtwenty = ["d20", 20]
    dhundred = ["d100", 100]
    coin = ["Coin flip", 2]