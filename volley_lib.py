from functools import lru_cache
from enum import Enum
from dataclasses import dataclass

# P and Q are global variables that should be set before calling these functions
P, Q = None, None

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
    return ret

def probXWins(pointsToWin, servingStrategy):
    return probXWinsPartial(State(pointsToWin, pointsToWin, True, servingStrategy))