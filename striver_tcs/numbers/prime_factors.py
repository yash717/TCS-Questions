def prime_factors(n):
    # Initialize an empty list to store the prime factors
    factors = []
    # Start with the smallest prime factor
    divisor = 2

    # Loop while 'n' is greater than 1
    while n > 1:
        # Check if 'n' is divisible by the current divisor
        while n % divisor == 0:
            # If divisible, append the divisor to the factors list
            factors.append(divisor)
            # Divide 'n' by the divisor until it's no longer divisible
            n //= divisor
        # Move to the next divisor
        divisor += 1

    # Return the list of prime factors
    return factors


# Test cases
n1 = 12
# Output: Prime factors of 12: [2, 2, 3]
print(f"Prime factors of {n1}: {prime_factors(n1)}")

n2 = 36
# Output: Prime factors of 36: [2, 2, 3, 3]
print(f"Prime factors of {n2}: {prime_factors(n2)}")
