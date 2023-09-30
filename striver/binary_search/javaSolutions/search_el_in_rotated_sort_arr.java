class Solution {

  public int search(int[] nums, int target) {
    // Initialize two pointers, left and right, to track the current search range.
    int left = 0;
    int right = nums.length - 1;

    // Perform binary search as long as left is less than or equal to right.
    while (left <= right) {
      // Calculate the middle index using binary search.
      int mid = left + (right - left) / 2;

      // Check if the middle element is equal to the target.
      if (nums[mid] == target) {
        return mid;
      }

      // Check if the left half is sorted.
      if (nums[left] <= nums[mid]) {
        // Check if the target is within the sorted left half.
        if (nums[left] <= target && target < nums[mid]) {
          right = mid - 1;
        } else {
          left = mid + 1;
        }
      }
      // If the left half is not sorted, the right half must be sorted.
      else {
        // Check if the target is within the sorted right half.
        if (nums[mid] < target && target <= nums[right]) {
          left = mid + 1;
        } else {
          right = mid - 1;
        }
      }
    }

    // If the target is not found, return -1.
    return -1;
  }
}
