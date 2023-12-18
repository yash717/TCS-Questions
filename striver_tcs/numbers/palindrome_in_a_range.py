# Function to reverse a number mathematically
def reverse_number(num):
    reversed_num = 0

    # Reverse the digits of the number
    while num > 0:
        # Get the last digit of the number
        digit = num % 10
        # Add the digit to the reversed number after multiplying it by 10
        reversed_num = reversed_num * 10 + digit
        # Update the number by removing the last digit
        num //= 10

    return reversed_num

# Function to find palindrome numbers within a given range


def find_palindromes_in_range(min_val, max_val):
    # Initialize an empty list to store palindrome numbers
    palindrome_list = []

    # Iterate through the range of numbers
    for num in range(min_val, max_val + 1):
        # Reverse the number
        reversed_num = reverse_number(num)

        # Check if the reversed number is equal to the original number
        if reversed_num == num:
            # If it's a palindrome, append it to the palindrome list
            palindrome_list.append(num)

    return palindrome_list


# Test Cases
min_val1, max_val1 = 10, 50
print(f"Palindromes in range {min_val1} to {max_val1}:")
print(find_palindromes_in_range(min_val1, max_val1))

min_val2, max_val2 = 100, 150
print(f"\nPalindromes in range {min_val2} to {max_val2}:")
print(find_palindromes_in_range(min_val2, max_val2))
