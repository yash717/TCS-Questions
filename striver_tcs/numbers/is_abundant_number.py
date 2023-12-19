def is_abundant(num):
    # Initialize the sum of divisors
    sum_divisors = 0

    # Calculate the sum of divisors
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i

    # Check if the sum of divisors is greater than the number
    if sum_divisors > num:
        return "Abundant Number"
    else:
        return "Not Abundant Number"


# Test case
print(is_abundant(96))  # Output: Abundant Number
