def are_anagrams(str1, str2):
    # Remove spaces and convert strings to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the lengths of the strings are equal
    if len(str1) != len(str2):
        return False

    # Create dictionaries to count characters in both strings
    count1 = {}
    count2 = {}

    # Count characters in first string
    for char in str1:
        if char in count1:
            count1[char] += 1
        else:
            count1[char] = 1

    # Count characters in second string
    for char in str2:
        if char in count2:
            count2[char] += 1
        else:
            count2[char] = 1

    # Check if both dictionaries are equal
    return count1 == count2


# Example usage
input_1 = "CAT"
input_2 = "ACT"

input_3 = "RULES"
input_4 = "LESRT"

print("Output 1:", are_anagrams(input_1, input_2))
print("Output 2:", are_anagrams(input_3, input_4))
