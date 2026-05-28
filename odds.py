import enum

class Odds(enum.Enum):
    Certain = 8
    Near_Certain = 7
    Very_Likely = 6
    Likely = 5
    Fifty_Fifty = 4
    Unlikely = 3
    Very_Unlikely = 2
    Nearly_Impossible = 1
    Impossible = 0


