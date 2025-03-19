from sympy import symbols, expand

def main():
    print("Hello from fantasy-volley!")

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


if __name__ == "__main__":
    main()
