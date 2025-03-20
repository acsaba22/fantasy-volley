from functools import lru_cache
from sympy import symbols, simplify
from enum import Enum
from dataclasses import dataclass

class ServingStrategy(Enum):
    WinnerServesNext = 0
    AlternateServing = 1

@dataclass(frozen=True)
class State:
    needX: int
    needY: int
    xServes: bool
    servingStrategy: ServingStrategy

    def Next(self, serverWon):
        needX = self.needX
        needY = self.needY
        if self.xServes:
            if serverWon:
                needX -= 1
            else:
                needY -= 1
        else:
            if serverWon:
                needY -= 1
            else:
                needX -= 1

        xServes = self.xServes
        if self.servingStrategy == ServingStrategy.WinnerServesNext:
            if not serverWon:
                xServes = not xServes
        else: # alternate
            xServes = not xServes

        return State(needX, needY, xServes, self.servingStrategy)

@lru_cache(maxsize=None)
def probXWinsPartial(state):
    global P, Q
    if state.needX == 0:
        return 1
    if state.needY == 0:
        return 0
    serverWins = P if state.xServes else Q

    return (serverWins * probXWinsPartial(state.Next(True))
            + (1 - serverWins) * probXWinsPartial(state.Next(False)))

def probXWins(pointsToWin, servingStrategy):
    return probXWinsPartial(State(pointsToWin, pointsToWin, True, servingStrategy))

def main():
    global P, Q
    P, Q = symbols('p q')
    print('WinerNext')
    n = 6
    # print(probXWinsPartial(State(1, 2, True, ServingStrategy.WinnerServesNext)))
    # print(probXWinsPartial(State(2, 1, False, ServingStrategy.WinnerServesNext)))
    a = probXWins(n, ServingStrategy.WinnerServesNext)
    # print(a)
    a = a.expand().simplify()
    # print(a)
    print('Alternate')
    # print(probXWinsPartial(State(1, 2, False, ServingStrategy.AlternateServing)))
    # print(probXWinsPartial(State(2, 1, False, ServingStrategy.AlternateServing)))
    b = probXWins(n, ServingStrategy.AlternateServing)
    # print(b)
    b = b.expand().simplify()
    # print(b)

    print(f"{a == b}")
    print(f"{a - b}")

if __name__ == "__main__":
    main()
