def is_armstrong_number(num):
    # Convert the number to a string to iterate through each digit
    num_str = str(num)
    # Calculate the length of the number (number of digits)
    num_len = len(num_str)

    # Initialize a variable to store the sum of cubes of digits
    armstrong_sum = 0

    # Iterate through each digit in the number
    for digit in num_str:
        # Convert the digit back to an integer and raise it to the power of the number of digits
        armstrong_sum += int(digit) ** num_len

    # Check if the calculated sum is equal to the original number
    if armstrong_sum == num:
        return "Yes, it is an Armstrong Number"
    else:
        return "No, it is not an Armstrong Number"


# Test cases
num1 = 153
print(f"Input: {num1}")
print(f"Output: {is_armstrong_number(num1)}")
# Output: Yes, it is an Armstrong Number

num2 = 170
print(f"\nInput: {num2}")
print(f"Output: {is_armstrong_number(num2)}")
# Output: No, it is not an Armstrong Number
