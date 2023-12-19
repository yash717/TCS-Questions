def min_max_digits(num):
    smallest_digit = 9
    largest_digit = 0

    # Iterate through each digit in the number
    while num > 0:
        digit = num % 10  # Extract the last digit

        # Update the smallest and largest digits if needed
        smallest_digit = min(smallest_digit, digit)
        largest_digit = max(largest_digit, digit)

        # Remove the last digit from the number
        num //= 10

    return largest_digit, smallest_digit


# Test cases
number1 = 2746
largest1, smallest1 = min_max_digits(number1)
print(f"Input: {number1}")
print(f"Largest digit: {largest1}")
print(f"Smallest digit: {smallest1}")
# Output: Largest digit: 7, Smallest digit: 2

number2 = 23004
largest2, smallest2 = min_max_digits(number2)
print(f"\nInput: {number2}")
print(f"Largest digit: {largest2}")
print(f"Smallest digit: {smallest2}")
# Output: Largest digit: 4, Smallest digit: 0
