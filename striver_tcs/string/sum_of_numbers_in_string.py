def find_sum(string):
    temp_sum = "0"  # Initialize a temporary string to store the currently forming number
    total_sum = 0   # Initialize the total sum of numbers found in the string

    for char in string:  # Iterate through each character in the input string
        if char.isdigit():  # Check if the character is a digit
            temp_sum += char  # If it's a digit, add it to the temporary sum to form a number
        else:
            # If it's not a digit, convert temp_sum to an integer and add it to the total sum
            total_sum += int(temp_sum)
            temp_sum = "0"  # Reset temp_sum to start forming a new number

    # Return the total sum of all numbers found in the string
    return total_sum + int(temp_sum)


# Example usage
input_str = "1bc268"
print("Sum:", find_sum(input_str))

