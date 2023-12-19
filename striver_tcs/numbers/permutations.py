def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(2, n + 1):
            fact *= i
        return fact


def permutations(n, r):
    numerator = factorial(n)
    denominator = factorial(n - r)
    perm_value = numerator // denominator

    return perm_value


# Test cases
N1, r1 = 5, 3
print(f"Permutations for {N1} people in {r1} seats:", permutations(
    N1, r1))  # Output: Permutations for 5 people in 3 seats: 60

N2, r2 = 6, 4
print(f"Permutations for {N2} people in {r2} seats:", permutations(
    N2, r2))  # Output: Permutations for 6 people in 4 seats: 360
