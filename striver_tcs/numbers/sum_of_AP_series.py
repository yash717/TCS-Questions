def sum_of_AP_series(n, a, d):
    # Formula to calculate the sum of an AP series: sum = n/2 * [2a + (n-1) * d]
    return (n / 2) * (2 * a + (n - 1) * d)

# Test cases
n1, a1, d1 = 4, 2, 2
print(f"Input: n={n1}, a={a1}, d={d1}")
print(f"Output: {int(sum_of_AP_series(n1, a1, d1))}")
# Output: 20

n2, a2, d2 = 8, 2, 5
print(f"\nInput: n={n2}, a={a2}, d={d2}")
print(f"Output: {int(sum_of_AP_series(n2, a2, d2))}")
# Output: 124
