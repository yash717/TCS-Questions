def fibonacci_recursive(n):
    # Base case: If n is less than or equal to 0, return an empty list
    if n <= 0:
        return []
    # Base case: If n is 1, return the first term of the Fibonacci series [0]
    elif n == 1:
        return [0]
    # Base case: If n is 2, return the first two terms of the Fibonacci series [0, 1]
    elif n == 2:
        return [0, 1]
    else:
        # Recursively call fibonacci_recursive to get the series up to (n - 1)th term
        series = fibonacci_recursive(n - 1)
        # Calculate the next number in the series and append it to the existing series
        series.append(series[-1] + series[-2])
        return series


# Test cases
N1 = 5
# Generate the Fibonacci series up to the N1th term
fib_series1 = fibonacci_recursive(N1)
print(f"Fibonacci series up to {N1}th term:", fib_series1)
# Output: Fibonacci series up to 5th term: [0, 1, 1, 2, 3]

N2 = 6
# Generate the Fibonacci series up to the N2th term
fib_series2 = fibonacci_recursive(N2)
print(f"\nFibonacci series up to {N2}th term:", fib_series2)
# Output: Fibonacci series up to 6th term: [0, 1, 1, 2, 3, 5]
