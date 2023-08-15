"""
Brute Force Approach:
The brute force approach involves iterating through the array and counting consecutive ones. We'll keep track of the maximum consecutive ones encountered and return that as the result.
Algorithm:

Initialize a variable max_ones to store the maximum consecutive ones encountered.
Initialize a variable current_ones to store the current count of consecutive ones while iterating through the array.
Iterate through the array nums:
If the current element is 1, increment current_ones.
If the current element is 0, update max_ones with the maximum value between max_ones and current_ones, and reset current_ones to 0.
After the loop ends, update max_ones with the maximum value between max_ones and current_ones one last time (in case the array ends with consecutive ones).
Return max_ones as the result."""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_ones = 0
        current_ones = 0

        for num in nums:
            if num == 1:
                current_ones += 1
            else:
                max_ones = max(max_ones, current_ones)
                current_ones = 0

        return max(max_ones, current_ones)


"""
Optimal Approach:
The optimal approach involves using a single loop to traverse the array and keep track of the maximum consecutive ones encountered so far. This eliminates the need to keep a separate  riable for the current count of consecutive ones.
Algorithm:

Initialize a variable max_ones to store the maximum consecutive ones encountered.
Initialize a variable current_ones to 0.
Iterate through the array nums:
If the current element is 1, increment current_ones and update max_ones with the maximum value between max_ones and current_ones.
If the current element is 0, reset current_ones to 0.
After the loop ends, max_ones will contain the maximum consecutive ones encountered in the array.
Return max_ones as the result.
Let's implement this optimal approach in code:"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_ones = 0
        current_ones = 0

        for num in nums:
            if num == 1:
                current_ones += 1
                max_ones = max(max_ones, current_ones)
            else:
                current_ones = 0

        return max_ones


"""
Both the brute force and optimal approaches have the same time complexity of O(n), where n is the length of the input array nums. However, the optimal approach uses less space as it only requires two variables (max_ones and current_ones) to keep track of the maximum consecutive ones encountered. Therefore, the optimal approach is preferred for efficiency."""
