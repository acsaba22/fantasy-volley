import volley_lib
from volley_lib import ServingStrategy, probXWins

def calculateNumeric(maxn, p_val=0.99, q_val=0.98):
    volley_lib.P, volley_lib.Q = p_val, q_val

    print(f'Calculating with numeric values (P={p_val}, Q={q_val})')

    for n in range(1, maxn+1):
        winner_serves = probXWins(n, ServingStrategy.WinnerServesNext)
        alternate = probXWins(n, ServingStrategy.AlternateServing)

        print(f"N={n} probability: {winner_serves:.6f}")

        difference = abs(winner_serves - alternate)
        if 0.01 < difference:
            raise ValueError(f"Values differ by {difference:.6f}, which exceeds threshold of 0.01")

if __name__ == "__main__":
    calculateNumeric(100)
