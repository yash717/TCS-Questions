# Solution 1: Using the "+" operator
# The "+" operator is used to concatenate strings in Python.

# Define two strings
str1 = "Hello"
str2 = "World"

# Concatenate the strings
result = str1 + str2

# Print the result
print("Result:", result)

# Output: HelloWorld

# Time Complexity: O(1)
# Space Complexity: O(1)


# Solution 2: Using library function "join"
# We can use the join() method to concatenate strings in Python.
# We create a list containing the strings we want to concatenate and then use the join() method to join them with an empty string.

# Define two strings
str1 = "Hello"
str2 = "World"

# Concatenate the strings
result = "".join([str1, str2])

# Print the result
print("Result:", result)

# Output: HelloWorld

# Time Complexity: O(n), where n is the total length of the concatenated strings
# Space Complexity: O(n), where n is the total length of the concatenated strings


# Solution 3: Using f-strings
# In Python 3.6 and above, we can use f-strings to concatenate strings.

# Define two strings
str1 = "Hello"
str2 = "World"

# Concatenate the strings using f-strings
result = f"{str1}{str2}"

# Print the result
print("Result:", result)

# Output: HelloWorld

# Time Complexity: O(1)
# Space Complexity: O(1)
