def capitalize_first_last(string):
    words = string.split()  # Split the string into words
    capitalized_words = []

    for word in words:
        if len(word) > 1:  # Check if the word has more than one character
            # Capitalize first and last character
            new_word = word[0].upper() + word[1:-1] + word[-1].upper()
            capitalized_words.append(new_word)
        else:
            # If the word has only one character, capitalize it
            capitalized_words.append(word.upper())

    # Join the words to form the final string
    return ' '.join(capitalized_words)


# Example usage
string_1 = "take u forward is awesome"
string_2 = "Take u Forward is Awesome"

print("Output 1:", capitalize_first_last(string_1))
print("Output 2:", capitalize_first_last(string_2))
