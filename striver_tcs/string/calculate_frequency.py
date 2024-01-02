def calculate_frequency(string):
    frequency = {}  # Create an empty dictionary to store character frequencies

    # Count frequency of characters
    for char in string:  # Iterate through each character in the input string
        if char in frequency:  # Check if the character is already in the dictionary
            frequency[char] += 1  # If yes, increment its count
        else:
            # If not, add the character to the dictionary with a count of 1
            frequency[char] = 1

    # Create the output string with character frequency
    output = ''  # Initialize an empty string for the output
    for char, count in frequency.items():  # Loop through the dictionary items (character, count)
        # Append each character and its count to the output string
        output += char + str(count) + ' '

    return output  # Return the final output string containing character frequencies


# Example usage
input_1 = "takeuforward"
input_2 = "articles"

print("Output 1:", calculate_frequency(input_1))
print("Output 2:", calculate_frequency(input_2))
