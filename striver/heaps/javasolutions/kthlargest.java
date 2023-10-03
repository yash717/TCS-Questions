import java.util.PriorityQueue;

class Solution {

  public int findKthLargest(int[] nums, int k) {
    // Create a min-heap to store the k largest elements
    PriorityQueue<Integer> minHeap = new PriorityQueue<>();

    // Initialize the min-heap with the first k elements
    for (int i = 0; i < k; i++) {
      minHeap.offer(nums[i]);
    }

    // Process the remaining elements
    for (int i = k; i < nums.length; i++) {
      // If the current element is larger than the smallest element in the heap,
      // replace the smallest element with the current element
      if (nums[i] > minHeap.peek()) {
        minHeap.poll();
        minHeap.offer(nums[i]);
      }
    }

    // The root of the min-heap will be the kth largest element
    return minHeap.peek();
  }
}
