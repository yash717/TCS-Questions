import heapq  # Import the heapq module for heap operations

# Define a function kthSmallLarge that takes an array arr, its size n, and k as input arguments


def kthSmallLarge(arr, n, k):

    # Create two heaps: min_heap for Kth smallest and max_heap for Kth largest
    min_heap = []  # Min-heap for Kth smallest
    max_heap = []  # Max-heap for Kth largest

    # Insert the first K elements from the array into both heaps
    for i in range(k):
        # Push element onto min_heap (default min-heap)
        heapq.heappush(min_heap, arr[i])
        # Push negative element onto max_heap (to simulate max-heap)
        heapq.heappush(max_heap, -arr[i])

    # Iterate through the remaining elements in the array
    for i in range(k, n):
        # Compare the current element with the root of the min-heap (Kth smallest)
        if arr[i] < min_heap[0]:
            # Remove the root element (smallest)
            heapq.heappop(min_heap)
            # Push the current element onto min_heap
            heapq.heappush(min_heap, arr[i])

        # Compare the current element with the root of the max-heap (Kth largest)
        if -arr[i] > max_heap[0]:
            # Remove the root element (largest, note the negative value)
            heapq.heappop(max_heap)
            # Push the negative of the current element onto max_heap
            heapq.heappush(max_heap, -arr[i])

    # The root of the min-heap will be the Kth smallest element
    kth_smallest = min_heap[0]
    # The root of the max-heap will be the Kth largest element (negated)
    kth_largest = -max_heap[0]

    # Return both the Kth smallest and Kth largest elements as a tuple
    return kth_smallest, kth_largest


# Example usage:
arr1 = [5, 6, 7, 2]
n1 = 4
k1 = 3
result1 = kthSmallLarge(arr1, n1, k1)  # Should return (7, 2)

arr2 = [1, 2, 5, 4]
n2 = 4
k2 = 3
result2 = kthSmallLarge(arr2, n2, k2)  # Should return (4, 2)
