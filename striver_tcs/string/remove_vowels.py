def remove_vowels(s):
    vowels = "aeiouAEIOU"
    result = ""
    for char in s:
        if char not in vowels:
            result += char
    return result


# Test cases
input_str_1 = "take u forward"
print(f"Input string: {input_str_1}, Output: {remove_vowels(input_str_1)}")

input_str_2 = "I am very happy today"
print(f"Input string: {input_str_2}, Output: {remove_vowels(input_str_2)}")
