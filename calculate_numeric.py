import volley_lib
from volley_lib import ServingStrategy, probXWins, probXWinsPartial

def calculateNumeric(maxn, p_val=0.99, q_val=0.98):
    # Set numeric values
    volley_lib.P, volley_lib.Q = p_val, q_val

    print(f'Calculating with numeric values (P={p_val}, Q={q_val})')

    for n in range(1, maxn+1):
        print(f"\nN = {n}")

        winner_serves = probXWins(n, ServingStrategy.WinnerServesNext)
        alternate = probXWins(n, ServingStrategy.AlternateServing)

        print(f"Winner serves next: {winner_serves:.6f}")
        print(f"Alternate serving: {alternate:.6f}")
        print(f"Difference: {abs(winner_serves - alternate):.10f}")

if __name__ == "__main__":
    calculateNumeric(8)