def is_match(s, p):
    """
    Check if a string matches a pattern where the pattern can contain wildcard characters '?' and '*'.

    Problem Statement:
    Given a string `s` and a pattern `p`, determine if `s` matches the pattern `p` where the pattern can contain wildcard characters:
        - '?' matches any single character.
        - '*' matches any sequence of characters (including the empty sequence).

    Parameters:
        s (str): The input string.
        p (str): The pattern string with wildcard characters.

    Returns:
        bool: True if the string matches the pattern, False otherwise.

    Examples:
        Example 1:
            Input: s = "aa", p = "a"
            Output: False
            Explanation: 'a' does not match 'aa'.

        Example 2:
            Input: s = "aa", p = "*"
            Output: True
            Explanation: '*' can match zero or more characters, so it matches 'aa'.

        Example 3:
            Input: s = "cb", p = "?a"
            Output: False
            Explanation: '?' does not match 'c'.

        Example 4:
            Input: s = "adceb", p = "*a*b"
            Output: True
            Explanation: '*' matches "dce", which is followed by 'a', then '*' matches "b".

        Example 5:
            Input: s = "acdcb", p = "a*c?b"
            Output: False
            Explanation: The character after 'c' cannot be determined.
    """
    # Initialize variables for string and pattern pointers
    s_ptr = 0
    p_ptr = 0
    # Initialize variables to store the positions of '*' and the characters after it
    star_ptr = -1
    match_ptr = -1

    # Loop through the string until the end is reached
    while s_ptr < len(s):
        # Case 1: If pattern pointer is within bounds and characters match or pattern has '?'
        if p_ptr < len(p) and (s[s_ptr] == p[p_ptr] or p[p_ptr] == '?'):
            # Move both pointers forward
            s_ptr += 1
            p_ptr += 1
        # Case 2: If pattern has '*', store the position and the current position after '*'
        elif p_ptr < len(p) and p[p_ptr] == '*':
            star_ptr = p_ptr
            match_ptr = s_ptr
            p_ptr += 1  # Move pattern pointer forward
        # Case 3: If there was a '*' before, try to match characters starting from last '*' position
        elif star_ptr != -1:
            p_ptr = star_ptr + 1  # Reset pattern pointer to after '*'
            match_ptr += 1  # Move string pointer forward
            s_ptr = match_ptr  # Reset string pointer to after matched position
        else:
            return False  # No match found, return False

    # If pattern has remaining '*' characters, skip them
    while p_ptr < len(p) and p[p_ptr] == '*':
        p_ptr += 1

    # If pattern pointer reached end, it means all characters in pattern matched
    return p_ptr == len(p)


# Test the function
s1 = "aa"
p1 = "a"
print(is_match(s1, p1))  # Output: False

s2 = "aa"
p2 = "*"
print(is_match(s2, p2))  # Output: True

s3 = "cb"
p3 = "?a"
print(is_match(s3, p3))  # Output: False

s4 = "adceb"
p4 = "*a*b"
print(is_match(s4, p4))  # Output: True

s5 = "acdcb"
p5 = "a*c?b"
print(is_match(s5, p5))  # Output: False
