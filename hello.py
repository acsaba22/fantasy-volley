from sympy import symbols, expand
import volley_probability

def demo_polynomial():
    print("\n--- Demonstrating polynomial multiplication ---")
    # Define symbolic variables
    x = symbols('x')
    
    # Create two polynomials
    poly1 = x**2 + 2*x + 1  # (x + 1)^2
    poly2 = x**2 - 1        # (x + 1)(x - 1)
    
    # Multiply the polynomials
    result = expand(poly1 * poly2)
    
    print(f"Polynomial 1: {poly1}")
    print(f"Polynomial 2: {poly2}")
    print(f"Result of multiplication: {result}")

def main():
    print("Hello from fantasy-volley!")
    
    # Run the polynomial example
    demo_polynomial()
    
    # Run the volley probability calculation
    print("\n--- Volley Tournament Probability ---")
    volley_probability.main()


if __name__ == "__main__":
    main()