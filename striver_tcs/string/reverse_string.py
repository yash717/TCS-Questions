def reverse_string(s):
    # Convert the string to a list
    s = list(s)

    # Set up pointers for reversing
    left, right = 0, len(s) - 1

    # Swap characters from both ends
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    # Convert the list back to a string
    return ''.join(s)


# Example usage
input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print("Original:", input_string)
print("Reversed:", reversed_string)
