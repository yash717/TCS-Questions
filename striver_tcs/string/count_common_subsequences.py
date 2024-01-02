def count_common_subsequences(S, T, m, n):
    # Base case: If either string is empty, there are no common subsequences
    if m == 0 or n == 0:
        return 0

    # If the last characters of both strings match
    elif S[m - 1] == T[n - 1]:
        # Recursively count common subsequences by considering the match and moving to the next characters
        return count_common_subsequences(S, T, m - 1, n - 1) + count_common_subsequences(S, T, m - 1, n) + 1

    # If the last characters of both strings don't match
    else:
        # Recursively count common subsequences by moving to the next character in the first string
        return count_common_subsequences(S, T, m - 1, n)

# Function wrapper for easy function call


def count_common(S, T):
    # Start the recursive counting process by passing the lengths of both strings
    return count_common_subsequences(S, T, len(S), len(T))


# Example usage
S1 = "ajblqcpdz"
T1 = "aefcnbtdi"

S2 = "aaab"
T2 = "ab"

# Output the count of common subsequences for strings S1 and T1
print("Output 1:", count_common(S1, T1))
# Output the count of common subsequences for strings S2 and T2
print("Output 2:", count_common(S2, T2))
