# Solution 1(Brute Force)
# Intuition: We just need to print the words in reverse order.
# Can we somehow store them in reverse order of the occurrence and then simply add it to our answer?

# Approach:
# Use a stack to push all the words in a stack
# Now, all the words of the string are present in the stack, but in reverse order
# Pop elements of the stack one by one and add them to our answer variable.
# Remember to add a space between the words as well.
def reverse_words_brute_force(s):
    # Add a space at the end to handle the last word
    s += " "
    stack = []  # Initialize a stack to store words
    word = ""   # Initialize an empty string to store a word
    # Iterate through each character in the string
    for char in s:
        if char == " ":  # If a space is encountered, it indicates the end of a word
            stack.append(word)  # Add the word to the stack
            word = ""   # Reset the word variable for the next word
        else:
            word += char  # If not a space, continue forming the word
    ans = ""    # Initialize an empty string for the final result
    # Pop elements of the stack one by one and add them to the answer variable
    while len(stack) > 1:
        ans += stack.pop() + " "  # Add word with a space
    ans += stack.pop()  # Add the last word without a space after it
    return ans


# Test case
s = "TUF is great for interview preparation"
print("Before reversing words:")
print(s)
print("After reversing words:")
print(reverse_words_brute_force(s))
# Output:
# Before reversing words:
# TUF is great for interview preparation
# After reversing words:
# preparation interview for great is TUF

# Time Complexity: O(N), Traversing the entire string
# Space Complexity: O(N), Stack and ans variable


# Solution 2(Optimized Solution)
# Intuition: Notice, that we are using a stack in order to perform our task.
# Can we somehow not use it and reverse the words as we move through the string?
# Could we store a word in reverse order when we are adding it to our answer variable?

# Approach:
# We start traversing the string from the end until we hit a space.
# It indicates that we have gone past a word and now we need to store it.
# We check if our answer variable is empty or not
# If it’s empty, it indicates that this is the last word we need to print,
# and hence, there shouldn’t be any space after this word.
# If it’s empty we add it to our result with a space after it.
def reverse_words_optimized(s):
    left = 0    # Initialize left pointer
    right = len(s) - 1  # Initialize right pointer
    temp = ""   # Initialize temporary string to store a word
    ans = ""    # Initialize final result string
    # Iterate through the string from left to right
    while left <= right:
        char = s[left]
        if char != "":  # If not a space, add the character to the temporary string
            temp += char
        elif char == "":  # If a space is encountered
            if ans:   # Check if the answer variable is empty
                ans = temp + " " + ans  # If not empty, add the word with a space to the answer
            else:
                ans = temp  # If empty, add the word without a space as it's the last word
            temp = ""   # Reset the temporary string for the next word
        left += 1   # Move to the next character
    # If not empty string then add to the result (Last word is added)
    if temp:
        if ans:
            ans = temp + " " + ans
        else:
            ans = temp
    return ans


# Test case
s = "TUF is great for interview preparation"
print("Before reversing words:")
print(s)
print("After reversing words:")
print(reverse_words_optimized(s))
# Output:
# Before reversing words:
# TUF is great for interview preparation
# After reversing words:
# preparation interview for great is TUF

# Time Complexity: O(N), where N is the length of the string
# Space Complexity: O(1), Constant Space
