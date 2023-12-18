def sum_of_GP_series(a, r, n):
    # Formula to calculate the sum of a GP series: sum = a * (1 - r^n) / (1 - r)
    return a * (1 - r**n) / (1 - r)

# Test cases
a1, r1, n1 = 1, 0.5, 3
print(f"Input: a={a1}, r={r1}, n={n1}")
print(f"Output: {sum_of_GP_series(a1, r1, n1)}")
# Output: 1.75

a2, r2, n2 = 3, 5, 2
print(f"\nInput: a={a2}, r={r2}, n={n2}")
print(f"Output: {sum_of_GP_series(a2, r2, n2)}")
# Output: 18
