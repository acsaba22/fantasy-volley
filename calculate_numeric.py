import volley_lib
from volley_lib import ServingStrategy, probXWins

def calculateNumeric(maxn, p_val=0.99, q_val=0.98):
    volley_lib.P, volley_lib.Q = p_val, q_val
    
    n_values = list(range(1, maxn+1))
    probabilities = []
    
    for n in n_values:
        winner_serves = probXWins(n, ServingStrategy.WinnerServesNext)
        alternate = probXWins(n, ServingStrategy.AlternateServing)
        
        difference = abs(winner_serves - alternate)
        if 0.01 < difference:
            raise ValueError(f"Values differ by {difference:.6f}, which exceeds threshold of 0.01")
        
        probabilities.append(float(winner_serves))
    
    return n_values, probabilities

def print_results(maxn=8, p_val=0.99, q_val=0.98):
    n_values, probabilities = calculateNumeric(maxn, p_val, q_val)
    
    print(f'Calculated with P={p_val}, Q={q_val}')
    for n, prob in zip(n_values, probabilities):
        print(f"N={n} probability: {prob:.6f}")

if __name__ == "__main__":
    print_results(8)
