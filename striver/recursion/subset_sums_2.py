"""CODING NINJA"""

"""The problem is asking for help in finding all the unique subsets of an array.
A subset is a collection of elements from the given array,
and two subsets are considered unique if they have a different set of elements.
The goal is to print all the unique subsets.
Now let's go through the provided code with comments explaining each line:"""




from typing import List
def uniqueSubsets(n: int, arr: List[int]) -> List[List[int]]:
    subsets = []
    arr.sort()  # Sort the array to handle duplicate elements

    generate_subsets(arr, n, 0, [], subsets)

    return subsets


def generate_subsets(arr, n, index, current_subset, subsets):
    # Append a copy of the current subset to subsets list
    subsets.append(current_subset[:])

    for i in range(index, n):
        # Skip duplicates to maintain uniqueness of subsets
        if i > index and arr[i] == arr[i-1]:
            continue

        # Include the current element in the subset
        current_subset.append(arr[i])
        # Recursively generate subsets
        generate_subsets(arr, n, i + 1, current_subset, subsets)
        current_subset.pop()  # Exclude the current element from the subset


"""In this code, the uniqueSubsets function takes the size n and the array arr as input and returns a list of unique subsets.
It initializes an empty list subsets to store the subsets.
The generate_subsets function is a recursive helper function that generates all the unique subsets. 
It takes the array arr, the size n, the current index, the current subset, and the subsets list as parameters.
It adds a copy of the current subset to the subsets list,
then iterates over the remaining elements starting from the current index.
It skips duplicates to maintain uniqueness of subsets.
For each element, it includes the element in the current subset, recursively generates subsets,
and then excludes the element from the current subset.

The driver code reads the input values, calls the uniqueSubsets function for each test case,
and prints the resulting subsets.

Note: The input reading and output printing are not included in the function uniqueSubsets.
You need to handle the input and output as per the problem statement."""


"""LEET CODE"""


class Solution(object):
    def subsetsWithDup(self, nums):
        subset = []  # Initialize an empty list to store the subsets
        nums.sort()  # Sort the array to handle duplicates
        # Call the recursive helper function to generate subsets
        self.generate_subsets(nums, 0, [], subset)
        return subset  # Return the list of subsets

    def generate_subsets(self, nums, index, current_subset, subset):
        n = len(nums)  # Get the length of the input array
        # Append a copy of the current subset to the subsets list
        subset.append(current_subset[:])

        for i in range(index, n):
            # Skip duplicates to avoid duplicate subsets
            if i > index and nums[i] == nums[i-1]:
                continue

            # Include the current element in the current subset
            current_subset.append(nums[i])
            # Recursively generate subsets
            self.generate_subsets(nums, i + 1, current_subset, subset)
            current_subset.pop()  # Exclude the current element from the current subset


"""Let's summarize the code's functionality:

The Solution class has a method named subsetsWithDup that takes the input array nums and returns a list of subsets.
It initializes an empty list subset to store the subsets.
The input array nums is sorted in ascending order using the sort() method to handle duplicates.
The generate_subsets method is a recursive helper function that generates all the subsets.
It takes the input array nums, the current index, the current subset, and the subsets list as parameters.
At the beginning of each recursive call, a copy of the current subset is appended to the subsets list.
The function iterates over the elements starting from the current index.
If the current element is a duplicate (not the first occurrence), it is skipped to avoid duplicate subsets.
For each element, it includes the element in the current subset,
recursively generates subsets, and then excludes the element from the current subset.
Finally, the subsetsWithDup method returns the list of subsets.
The code effectively generates all possible subsets while avoiding duplicates by skipping duplicate elements."""
