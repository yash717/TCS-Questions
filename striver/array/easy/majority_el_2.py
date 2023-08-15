"""
class Solution(object):: The code is defined inside a class called Solution. It's a common practice when using LeetCode-style problem templates, but it's not necessary for understanding the logic.

def majorityElement(self, nums):: This is the function definition for majorityElement. It takes one parameter nums, which represents the input array. It returns an integer, which is the majority element.

counter = {}: We initialize an empty dictionary called counter to store the frequency of each element.

for num in nums:: We iterate through each element in the nums array.

if num in counter: counter[num] += 1: If the element num is already present in the counter dictionary, we increment its count by 1.

else: counter[num] = 1: If the element num is not present in the counter dictionary, we add it with a count of 1.

majority = max(counter, key=counter.get): We use the max function with the key parameter set to counter.get to find the element with the highest frequency in the counter dictionary.

return majority: Finally, we return the majority element.

This solution has a time complexity of O(n) because we iterate through the array once to count the occurrences of each element and find the majority element."""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Step 1: Initialize a counter dictionary to store the frequency of each element
        counter = {}

        # Step 2: Iterate through the array and count the occurrences of each element
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        # Step 3: Find the element with the highest frequency
        majority = max(counter, key=counter.get)

        # Step 4: Return the majority element
        return majority
