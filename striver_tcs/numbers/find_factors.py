def find_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors


# Test cases
n1 = 6
# Output: Factors of 6: [1, 2, 3, 6]
print(f"Factors of {n1}: {find_factors(n1)}")

n2 = 9
# Output: Factors of 9: [1, 3, 9]
print(f"Factors of {n2}: {find_factors(n2)}")
