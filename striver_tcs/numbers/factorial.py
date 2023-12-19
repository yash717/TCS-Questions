def factorial_iterative(X):
    # If X is 0 or 1, factorial is 1 (0! = 1! = 1)
    if X == 0 or X == 1:
        return 1
    else:
        fact = 1  # Initialize the factorial value as 1
        # Calculate factorial iteratively from 2 to X
        for i in range(2, X + 1):
            fact *= i  # Multiply fact by each number from 2 to X
        return fact  # Return the final factorial result


def factorial_recursive(X):
    # Base case: If X is 0 or 1, return 1 (0! = 1! = 1)
    if X == 0 or X == 1:
        return 1
    else:
        # Recursive call to compute factorial by multiplying X with factorial_recursive(X - 1)
        # This step computes factorial by breaking down the problem into smaller subproblems
        return X * factorial_recursive(X - 1)


# Test cases
X1 = 5
print("Factorial of", X1, ":", factorial_recursive(X1))  # Output: 120

X2 = 3
print("Factorial of", X2, ":", factorial_recursive(X2))  # Output: 6


# Test cases
X1 = 5
print("Factorial of", X1, ":", factorial_iterative(X1))  # Output: 120

X2 = 3
print("Factorial of", X2, ":", factorial_iterative(X2))  # Output: 6
