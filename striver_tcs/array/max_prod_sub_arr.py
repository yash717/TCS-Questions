def maxProductSubArray(arr):
    n = len(arr)  # Get the size of the array

    # Initialize maximum product subarray to negative infinity
    max_product = 1
    # Initialize prefix and suffix products to 1
    prefix_product, suffix_product = 1, 1

    for i in range(n):  # Loop through each element in the array
        # Ensure that a zero value doesn't affect the product calculation
        if prefix_product == 0:
            prefix_product = 1
        if suffix_product == 0:
            suffix_product = 1

        # Update prefix product by multiplying with the current element
        prefix_product *= arr[i]
        # Update suffix product by multiplying with the current element from the end
        suffix_product *= arr[n - i - 1]

        # Update max product using the maximum of prefix and suffix products
        max_product = max(max_product, max(prefix_product, suffix_product))

    return max_product  # Return the maximum product subarray


arr = [1, 2, -3, 0, -4, -5]  # Sample array
result = maxProductSubArray(arr)  # Get the maximum product subarray
print("The maximum product subarray is:", result)  # Print the result
