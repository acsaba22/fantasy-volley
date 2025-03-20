from sympy import symbols
import volley_lib
from volley_lib import ServingStrategy, probXWins

def calculateSymbolic(maxn):
    print('Calculating with polynomials')

    volley_lib.P, volley_lib.Q = symbols('p q')

    for n in range(1, maxn+1):
        print(f"\nN = {n}")
        a = probXWins(n, ServingStrategy.WinnerServesNext)
        a = a.expand().simplify()
        b = probXWins(n, ServingStrategy.AlternateServing)
        b = b.expand().simplify()

        print(f"Equal: {a == b}")
        print(f"Result: {a}")

        print(f"Value: {float(a.subs({volley_lib.P: 0.99, volley_lib.Q: 0.98})):.6f}")

if __name__ == "__main__":
    calculateSymbolic(8)