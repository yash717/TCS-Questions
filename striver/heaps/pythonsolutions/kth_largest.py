import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        # Create a min-heap to store the k largest elements
        min_heap = []

        # Initialize the min-heap with the first k elements
        for num in nums[:k]:
            heapq.heappush(min_heap, num)

        # Process the remaining elements
        for num in nums[k:]:
            # If the current element is larger than the smallest element in the heap,
            # replace the smallest element with the current element
            if num > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)

        # The root of the min-heap will be the kth largest element
        return min_heap[0]
