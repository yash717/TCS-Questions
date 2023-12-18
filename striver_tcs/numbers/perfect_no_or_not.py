def is_perfect_number(num):
    # Initialize the variable to store the sum of divisors
    divisors_sum = 0

    # Iterate from 1 to num//2 (as divisors are checked only until half of the number)
    for i in range(1, num // 2 + 1):
        # Check if i is a divisor of num
        if num % i == 0:
            # Add the divisor to the sum of divisors
            divisors_sum += i

    # Check if the sum of divisors is equal to the number itself
    if divisors_sum == num:
        return f"{num} is a perfect number"
    else:
        return f"{num} is not a perfect number"


# Test cases
num1 = 6
print(f"Input: n={num1}")
print(f"Output: {is_perfect_number(num1)}")
# Output: 6 is a perfect number

num2 = 15
print(f"\nInput: n={num2}")
print(f"Output: {is_perfect_number(num2)}")
# Output: 15 is not a perfect number

num3 = 28
print(f"\nInput: n={num3}")
print(f"Output: {is_perfect_number(num3)}")
# Output: 28 is a perfect number
