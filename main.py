from functools import lru_cache
from sympy import symbols
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

    ret = (serverWins * probXWinsPartial(state.Next(True))
           + (1 - serverWins) * probXWinsPartial(state.Next(False)))
    # ret = ret.expand().simplify() # makes it even slover and doesn't work for numbers
    return ret

def probXWins(pointsToWin, servingStrategy):
    return probXWinsPartial(State(pointsToWin, pointsToWin, True, servingStrategy))


def calculateSymbolic(maxn):
    print('Calculating with polinoms')

    global P, Q
    P, Q = symbols('p q')

    for n in range(1, maxn+1):
        print(f"\nN = {n}")
        a = probXWins(n, ServingStrategy.WinnerServesNext)
        a = a.expand().simplify()
        b = probXWins(n, ServingStrategy.AlternateServing)
        b = b.expand().simplify()

        print(f"Equal: {a == b}")
        print(f"Result: {a}")

        # Print with 6 decimal places
        print(f"Value: {float(a.subs({P: 0.99, Q: 0.98})):.6f}")

def calculatNumeric():
    global P, Q
    P, Q = 0.99, 0.98
    a = probXWins(30, ServingStrategy.WinnerServesNext)
    print(a)
    pass

def main():
    calculateSymbolic(3)
    probXWinsPartial.cache_clear()
    calculatNumeric()

    pass

if __name__ == "__main__":
    main()
