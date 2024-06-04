def change_case(s: str) -> str:
    """
    Change the case of each character in a given string.

    Parameters:
        s (str): The input string.

    Returns:
        str: The string with changed case.
    """
    result = ""
    for char in s:
        # If the character is uppercase, convert it to lowercase
        if char.isupper():
            result += char.lower()
        # If the character is lowercase, convert it to uppercase
        elif char.islower():
            result += char.upper()
        # If it's a whitespace, keep it as it is
        else:
            result += char

    return result


# Test cases
s1 = "javA"
print("\nExample 1:")
print("Input:", s1)
print("Output:", change_case(s1))  # Output: JAVa

s2 = "take u forward IS Awesome"
print("\nExample 2:")
print("Input:", s2)
print("Output:", change_case(s2))  # Output: TAKE U FORWARD is aWESOME
