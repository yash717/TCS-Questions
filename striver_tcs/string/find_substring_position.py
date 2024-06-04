# Solution 1: Naive Approach
# We can use a brute-force approach to find the position of a substring within a string.
# We iterate through the main string and check if the substring matches starting from each position.
# If a match is found, we return the starting index of the substring in the main string.
# If no match is found, we return -1.

def find_substring_position(text, pattern):
    N = len(text)
    M = len(pattern)

    for i in range(N - M + 1):
        temp = i
        for j in range(M):
            if text[temp] != pattern[j]:
                break
            temp += 1
        if j == M - 1:
            return i

    return -1


# Test case
text = "takeuforward"
pattern = "forward"
found_idx = find_substring_position(text, pattern)
print("The substring starts from the index:", found_idx)
# Output: The substring starts from the index: 5

# Time Complexity: O(N^2)
# Space Complexity: O(1)

# Solution 2: Using Library Functions
# We can use built-in functions like find() in C++ and indexOf() in Java to find the position of a substring within a string.
# These functions search for the first occurrence of the substring in the string and return its starting index.

# In Python, we can use the find() method.


def find_substring_position(text, pattern):
    found_idx = text.find(pattern)
    return found_idx


# Test case
text = "takeuforward"
pattern = "forward"
found_idx = find_substring_position(text, pattern)
print("The substring starts from the index:", found_idx)
# Output: The substring starts from the index: 5

# Time Complexity: O(N)
# Space Complexity: O(1)
