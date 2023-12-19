def gcd(num1, num2):
    # Initialize the greatest common divisor (GCD) to 1
    gcd = 1

    # Iterate from 1 to the minimum of the two numbers
    for i in range(1, min(num1, num2) + 1):
        # Check if 'i' is a common divisor for both 'num1' and 'num2'
        if num1 % i == 0 and num2 % i == 0:
            gcd = i  # Update GCD if 'i' is a common divisor

    return gcd  # Return the greatest common divisor


def addFractions(a, b, c, d):
    # Calculate the numerators and the common denominator
    num1 = a * d
    num2 = b * c
    den = b * d

    # Sum of the numerators
    num_final = num1 + num2

    # Find the greatest common divisor of the numerator and denominator
    gcd1 = gcd(num_final, den)

    # Simplify the fraction by dividing both the numerator and denominator by their GCD
    num_final //= gcd1
    den //= gcd1

    # Return the result in the form of a string
    return f"{num_final}/{den}"


# Test the gcd function with values 12 and 4
print(gcd(12, 4))

# Test cases for adding fractions
print("3/4 + 1/7 =", addFractions(3, 4, 1, 7))  # Output: 25/28
print("5/2 + 1/2 =", addFractions(5, 2, 1, 2))  # Output: 3/1
