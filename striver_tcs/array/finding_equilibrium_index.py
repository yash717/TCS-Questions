def findEquilibriumIndex(nums):
    # Calculate the total sum of the array
    total_sum = sum(nums)
    left_sum = 0  # Initialize left_sum

    # Iterate through each element in the array
    for i in range(len(nums)):
        # Check if left_sum is equal to the right sum
        if left_sum == total_sum - nums[i] - left_sum:
            return i  # Return the equilibrium index if found
        left_sum += nums[i]  # Update left_sum

    return -1  # Return -1 if no equilibrium index is found


# Driver code to test the function
nums1 = [2, 3, -1, 8, 4]
print("Example 1:")
print("Input:", nums1)
result1 = findEquilibriumIndex(nums1)
print("Output:", result1)

nums2 = [1, -1, 4]
print("\nExample 2:")
print("Input:", nums2)
result2 = findEquilibriumIndex(nums2)
print("Output:", result2)
