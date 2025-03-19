"""
Calculate the probability of winning in a mathematically perfect Volley Tournament.

Two teams play a series of rallies until one wins N points.
Team X has probability P of winning a rally when serving.
Team Y has probability Q of winning a rally when serving.
Team X serves first, and teams alternate serving after each rally.
"""

import numpy as np
from sympy import symbols, Matrix, simplify, S

def calculate_win_probability_numerical(p, q, n):
    """
    Calculate the probability that team X wins using numerical methods.
    
    Args:
        p: Probability that team X wins a rally when serving
        q: Probability that team Y wins a rally when serving
        n: Number of points needed to win
        
    Returns:
        Probability that team X wins the match
    """
    # States are represented as (x_score, y_score, serving_team)
    # where serving_team is 0 for X and 1 for Y
    
    # Create a dictionary to store state -> index mapping
    states = {}
    index = 0
    
    # Generate all possible states
    for x_score in range(n + 1):
        for y_score in range(n + 1):
            if x_score == n and y_score == n:
                # Both can't have winning score
                continue
            for serving in [0, 1]:
                states[(x_score, y_score, serving)] = index
                index += 1
    
    # Total number of states
    num_states = len(states)
    
    # Create transition probability matrix
    P = np.zeros((num_states, num_states))
    
    # Terminal states for X winning and Y winning
    x_win_state = states.get((n, 0, 0), None)  # Arbitrary terminal state for X winning
    y_win_state = states.get((0, n, 0), None)  # Arbitrary terminal state for Y winning
    
    # Fill in transition probabilities
    for state, i in states.items():
        x_score, y_score, serving = state
        
        # Terminal states
        if x_score == n or y_score == n:
            P[i, i] = 1.0  # Stay in the same state with probability 1
            continue
        
        # Team X is serving
        if serving == 0:
            # X wins the rally with probability p
            next_state = (x_score + 1, y_score, 0 if x_score + 1 < n else 0)
            if x_score + 1 == n:
                next_state_idx = x_win_state
            else:
                next_state_idx = states[next_state]
            P[i, next_state_idx] = p
            
            # Y wins the rally with probability (1-p)
            next_state = (x_score, y_score + 1, 1)
            if y_score + 1 == n:
                next_state_idx = y_win_state
            else:
                next_state_idx = states[next_state]
            P[i, next_state_idx] = 1 - p
        
        # Team Y is serving
        else:
            # X wins the rally with probability (1-q)
            next_state = (x_score + 1, y_score, 0)
            if x_score + 1 == n:
                next_state_idx = x_win_state
            else:
                next_state_idx = states[next_state]
            P[i, next_state_idx] = 1 - q
            
            # Y wins the rally with probability q
            next_state = (x_score, y_score + 1, 1 if y_score + 1 < n else 1)
            if y_score + 1 == n:
                next_state_idx = y_win_state
            else:
                next_state_idx = states[next_state]
            P[i, next_state_idx] = q
    
    # Initial state: (0, 0, 0) - scores are 0-0 and X is serving
    initial_state_idx = states[(0, 0, 0)]
    
    # Create initial probability distribution
    initial_dist = np.zeros(num_states)
    initial_dist[initial_state_idx] = 1.0
    
    # Compute absorption probabilities
    # We need to find the probability of reaching x_win_state from initial_state_idx
    
    # Separate transient and absorbing states
    transient_indices = [i for (state, i) in states.items() 
                         if state[0] < n and state[1] < n]
    absorbing_indices = [i for i in range(num_states) if i not in transient_indices]
    
    # Reorder the matrix to put transient states first, then absorbing states
    order = transient_indices + absorbing_indices
    P_ordered = P[order, :][:, order]
    
    # Extract the submatrices
    n_transient = len(transient_indices)
    Q = P_ordered[:n_transient, :n_transient]  # Transitions between transient states
    R = P_ordered[:n_transient, n_transient:]  # Transitions from transient to absorbing
    
    # Compute the fundamental matrix
    I = np.eye(n_transient)
    N = np.linalg.inv(I - Q)
    
    # Compute absorption probabilities
    B = np.dot(N, R)
    
    # Find the index of the initial state in the reordered matrix
    initial_idx_reordered = order.index(initial_state_idx)
    
    # Find the index of X's winning state in the absorbing states
    x_win_idx_absorbing = absorbing_indices.index(x_win_state)
    
    # Probability that X wins
    prob_x_wins = B[initial_idx_reordered, x_win_idx_absorbing]
    
    return prob_x_wins

def calculate_win_probability_symbolic(n):
    """
    Calculate the symbolic probability that team X wins.
    
    Args:
        n: Number of points needed to win
        
    Returns:
        Symbolic expression for the probability that team X wins
    """
    # This is a simplified implementation for small n
    # For larger n, the symbolic computation becomes too complex
    
    p, q = symbols('p q')
    
    # For n=1, X wins with probability p (since X serves first)
    if n == 1:
        return p
    
    # For n=2, calculate the probability using direct calculation
    if n == 2:
        # X wins in one of these ways:
        # 1. X serves & wins + X serves & wins: p * p
        # 2. X serves & wins + X serves & loses + Y serves & loses + X serves & wins: p * (1-p) * (1-q) * p
        # 3. X serves & loses + Y serves & loses + X serves & wins + X serves & wins: (1-p) * (1-q) * p * p
        # 4. X serves & loses + Y serves & wins + Y serves & loses + X serves & wins + X serves & wins: 
        #    (1-p) * q * (1-q) * (1-q) * p
        
        term1 = p * p
        term2 = p * (1-p) * (1-q) * p
        term3 = (1-p) * (1-q) * p * p
        term4 = (1-p) * q * (1-q) * (1-q) * p
        
        return simplify(term1 + term2 + term3 + term4)
    
    # For larger n, we need to implement a more efficient approach
    # such as solving recurrence relations or using generating functions
    return S("Symbol('solution_for_n_{n}')").subs('n', n)

def main():
    # Example parameters
    p = 0.99  # Probability X wins when serving
    q = 0.98  # Probability Y wins when serving
    n = 2     # Points needed to win
    
    # Calculate the numerical probability
    prob_num = calculate_win_probability_numerical(p, q, n)
    print(f"Probability that team X wins (numerical, n={n}): {prob_num:.6f}")
    
    # Calculate the symbolic probability for small n
    for n_val in [1, 2]:
        prob_sym = calculate_win_probability_symbolic(n_val)
        print(f"Symbolic probability for n={n_val}: {simplify(prob_sym)}")
    
    # Show numerical results for larger values of n
    for n_val in [5, 10, 25, 50, 100]:
        prob = calculate_win_probability_numerical(p, q, n_val)
        print(f"Probability that team X wins (n={n_val}): {prob:.6f}")

if __name__ == "__main__":
    main()