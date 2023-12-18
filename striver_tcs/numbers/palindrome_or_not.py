def isPalindrome(N):
    original = N  # Store the original number for comparison later
    reverse = 0  # Initialize a variable to store the reverse of the number

    # Loop to reverse the number
    while N > 0:
        digit = N % 10  # Extract the last digit
        reverse = reverse * 10 + digit  # Build the reverse number
        N = N // 10  # Remove the last digit

    # Check if the original number and its reverse are the same
    if original == reverse:
        return "Palindrome Number"  # If they match, it's a palindrome
    else:
        return "Not Palindrome Number"  # If they don't match, it's not a palindrome


# Test cases
num1 = 123
print(f"Output for Example 1: {isPalindrome(num1)}")

num2 = 121
print(f"Output for Example 2: {isPalindrome(num2)}")
