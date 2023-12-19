def is_palindrome(s):
    # Remove spaces and convert string to lowercase
    s = s.replace(" ", "").lower()

    # Initialize pointers for start and end of the string
    start = 0
    end = len(s) - 1

    # Check characters from start and end towards the center
    while start < end:
        # If characters at start and end are not equal, it's not a palindrome
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1

    return True


# Test cases
string1 = "ABCDCBA"
if is_palindrome(string1):
    print("Palindrome")
else:
    print("Not Palindrome")

string2 = "TAKE U FORWARD"
if is_palindrome(string2):
    print("Palindrome")
else:
    print("Not Palindrome")
