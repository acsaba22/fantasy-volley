from functools import lru_cache
from sympy import symbols, simplify
from enum import Enum

class ServingStrategy(Enum):
    WinnerServesNext = 0
    AlternateServing = 1

@lru_cache(maxsize=None)
def probXWinsPartial(needX, needY, xServes, servingStrategy):
    global P, Q
    if needX == 0:
        return 1
    if needY == 0:
        return 0
    p, q = (P, Q) if xServes else (Q, P)

    ret = 0

    return 1

def probXWins(pointsToWin, servingStrategy):
    return probXWinsPartial(pointsToWin, pointsToWin, True, servingStrategy)

def main():
    global P, Q
    P, Q = symbols('p q')
    print(probXWins(1, ServingStrategy.AlternateServing))

if __name__ == "__main__":
    main()