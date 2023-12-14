def nonRepeating(arr):
    frequencies = {}
    non_repeating = []

    for i in arr:
        frequencies[i] = frequencies.get(i, 0)+1

    for i, count in frequencies.items():
        if count == 1:
            non_repeating.append(i)

    return non_repeating


# Example 1
arr1 = [1, 2, -1, 1, 3, 1]
result1 = nonRepeating(arr1)
print("Example 1:")
print("Output:", result1)

# Example 2
arr2 = [1, 2, 3]
result2 = nonRepeating(arr2)
print("\nExample 2:")
print("Output:", result2)


def findNonRepeatingElements(nums):
    frequency = {}  # Create an empty dictionary to store element frequencies
    non_repeating_elements = []  # Create an empty list to store non-repeating elements

    # Count occurrences of each element in the array
    for num in nums:
        # Increment count of 'num' in the frequency dictionary
        frequency[num] = frequency.get(num, 0) + 1
    
    # Collect elements with count 1 (non-repeating)
    for num, count in frequency.items():
        if count == 1:  # If the count of the element is 1 (occurs only once)
            # Add the element to the list of non-repeating elements
            non_repeating_elements.append(num)

    return non_repeating_elements  # Return the list of non-repeating elements
