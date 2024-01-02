def print_frequency(st):
    freq = {}  # Initialize a dictionary to store character frequencies

    # Loop through each character in the input string to count frequencies
    for char in st:
        if char != ' ':  # Exclude spaces from frequency counting
            # Increment the frequency count of each character
            freq[char] = freq.get(char, 0) + 1

    # Printing the non-repeating characters
    for char in st:  # Loop through each character in the input string again
        # Check if the character is non-space and occurs only once
        if char != ' ' and freq[char] == 1:
            print(char, end=' ')  # If yes, print the non-repeating character


# Example usage
st = "take u forward"
print("Non-Repeating characters:", end=' ')
print_frequency(st)
