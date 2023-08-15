# brute force

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Initialize the result list to store the triplets that sum up to zero
        result = []

        # Loop through all possible combinations of triplets
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    # Check if the sum of the current triplet is equal to zero
                    if nums[i] + nums[j] + nums[k] == 0:
                        # Create a list with the triplet elements and append it to the result list
                        triplet = [nums[i], nums[j], nums[k]]
                        result.append(triplet)

        # Return the final result list
        return result


#optimal solution

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Sort the array in ascending order
        nums.sort()
        result = []  # Initialize an empty list to store the triplets

        for i in range(len(nums) - 2):
            # Skip duplicates for i pointer
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Initialize left and right pointers
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    # If the sum of three numbers equals zero, add the triplet to the result
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for left and right pointers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif total < 0:
                    # If the sum is less than zero, increment the left pointer
                    left += 1
                else:
                    # If the sum is greater than zero, decrement the right pointer
                    right -= 1

        return result


"""
We sort the input nums array in ascending order. Sorting is necessary to apply the two-pointer approach.
We initialize an empty list result to store the triplets that sum up to zero.
We use a for loop to iterate over the nums array. The loop goes from the first element to the second-to-last element (i.e., len(nums) - 2) because we need at least three elements to form a triplet.
Inside the loop, we check for duplicates using the if condition. If the current element (nums[i]) is the same as the previous element (nums[i - 1]) and i is greater than zero, it means we have already considered the triplet with this element. So, we continue to the next iteration.
We initialize two pointers, left and right, for the two-pointer approach. left starts from the next index of i, and right starts from the last index of the array.
We enter a while loop, which continues as long as left is less than right. In each iteration of the while loop, we calculate the total sum of the current triplet: nums[i] + nums[left] + nums[right].
If the total is equal to zero, it means we have found a triplet that sums up to zero. We add this triplet to the result list.
After adding the triplet to the result, we skip any duplicates for the left and right pointers. We increment left while its value is the same as the next element (nums[left + 1]) and decrement right while its value is the same as the previous element (nums[right - 1]).
We then increment left and decrement right to move towards the center of the sorted array.
If the total is less than zero, it means the sum of the current triplet is too small, and we need to increase the sum. So, we increment the left pointer.
If the total is greater than zero, it means the sum of the current triplet is too large, and we need to decrease the sum. So, we decrement the right pointer.
The while loop continues until the left pointer is less than the right pointer.
Once the for loop completes, we have found all the triplets that sum up to zero, and we return the result list containing these triplets.
The two-pointer approach significantly reduces the time complexity of finding triplets that sum up to zero from O(n^3) (in a brute-force approach) to O(n^2)."""
