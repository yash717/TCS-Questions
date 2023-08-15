"""PROBLEM STATEMENT"""
"""You are given an array ‘Arr’ of ‘N’ positive integers. You are also given a positive integer ‘target’.
Your task is to find all unique combinations of the array ‘Arr’ whose sum is equal to ‘target’.
Each number in ‘Arr’ may only be used once in the combination.
Elements in each combination must be in non-decreasing order and you need to print all unique combinations in
lexicographical order."""

"""PROBLEM STATEMENT EXPLANATION"""

"""You are given an array Arr of N positive integers and a positive integer target.
The goal is to find all unique combinations of the array Arr whose sum is equal to the target.
Each number in Arr can only be used once in a combination.

Here are the conditions for the combinations:

Elements in each combination must be in non-decreasing order.
This means the numbers in each combination should be arranged in ascending order.

The unique combinations should be printed in lexicographical order. 
In lexicographical order, combination/array 'A' comes before array 'B' if 'A' is the prefix of array 'B',
or if none of them is a prefix of the other and at the first position where they differ,
the integer in 'A' is smaller than the integer in 'B'.

For example, let's consider an input scenario:

Array Arr: [1, 2, 3, 1]
Target: 5

In this case, the possible valid combinations in lexicographical order are:

(1, 1, 3)
(2, 3)

Now, let's break down the input format and constraints:

Input Format:

The first line of input contains an integer T denoting the number of test cases.
For each test case, the first line contains two space-separated integers N and target,
representing the number of elements in Arr and the target sum, respectively.
The second line of each test case contains N space-separated integers, the elements of the array Arr."""


"""STRIVER CODE"""




from typing import List
def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    ans = []  # List to store the final combinations
    ds = []  # List to store the current combination being formed
    candidates.sort()  # Sort the candidates in non-decreasing order

    def findCombination(ind: int, target: int):
        """
        Recursive function to find unique combinations of candidates that sum up to the target.
        Parameters:
        - ind: Current index of the candidate being considered
        - target: Remaining target sum to be achieved
        """
        if target == 0:  # Base case: If the target sum is achieved
            # Add the current combination to the final answer
            ans.append(ds[:])
            return

        for i in range(ind, len(candidates)):
            # Skip duplicates to avoid duplicate combinations
            if i > ind and candidates[i] == candidates[i - 1]:
                continue

            if candidates[i] > target:
                break  # Since the candidates are sorted, no further combination is possible

            # Include the current candidate in the combination
            ds.append(candidates[i])
            # Recursively find the remaining combination
            findCombination(i + 1, target - candidates[i])
            ds.pop()  # Backtrack by removing the current candidate from the combination

    # Start the recursive combination finding process
    findCombination(0, target)
    return ans  # Return the final combinations


if __name__ == "__main__":
    v = [10, 1, 2, 7, 6, 1, 5]
    comb = combinationSum2(v, 8)
    print(*comb)


"""coding ninja code"""


def combinationSum2(arr, n, target):
    arr.sort()  # Sort the array in non-decreasing order
    combinations = []  # List to store the final combinations
    # Call the helper function to find combinations
    find_combinations(arr, n, target, 0, [], combinations)
    return combinations  # Return the final combinations


def find_combinations(arr, n, target, index, current_combination, combinations):
    """
    Helper function to find unique combinations of arr that sum up to the target.
    Parameters:
    - arr: List of positive integers
    - n: Number of elements in arr
    - target: Remaining target sum to be achieved
    - index: Current index of the element being considered
    - current_combination: List to store the current combination being formed
    - combinations: List to store the final combinations
    """
    if target == 0:  # Base case: If the target sum is achieved
        # Add the current combination to the final combinations
        combinations.append(current_combination[:])
        return

    if index == n or target < 0:
        return  # Base case: If the end of the array is reached or the target sum becomes negative, backtrack

    for i in range(index, n):
        # Skip duplicates to avoid duplicate combinations
        if i > index and arr[i] == arr[i - 1]:
            continue

        # Include the current element in the combination
        current_combination.append(arr[i])
        # Recursively find the remaining combination
        find_combinations(
            arr, n, target - arr[i], i + 1, current_combination, combinations)
        # Backtrack by removing the current element from the combination
        current_combination.pop()


"""leetcode solution"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()  # Sort the candidates in non-decreasing order
        combinations = []  # List to store the final combinations
        # Call the helper function to find combinations
        self.find_combinations(candidates, target, 0, [], combinations)
        return combinations  # Return the final combinations

    def find_combinations(self, candidates, target, index, current_combination, combinations):
        """
        Helper function to find unique combinations of candidates that sum up to the target.
        Parameters:
        - candidates: List of positive integers
        - target: Remaining target sum to be achieved
        - index: Current index of the candidate being considered
        - current_combination: List to store the current combination being formed
        - combinations: List to store the final combinations
        """
        if target == 0:  # Base case: If the target sum is achieved
            # Add the current combination to the final combinations
            combinations.append(current_combination[:])
            return

        if index == len(candidates) or target < 0:
            return  # Base case: If the end of the candidates list is reached or the target sum becomes negative, backtrack

        for i in range(index, len(candidates)):
            # Skip duplicates to avoid duplicate combinations
            if i > index and candidates[i] == candidates[i - 1]:
                continue

            # Include the current candidate in the combination
            current_combination.append(candidates[i])
            # Recursively find the remaining combination
            self.find_combinations(
                candidates, target - candidates[i], i + 1, current_combination, combinations)
            # Backtrack by removing the current candidate from the combination
            current_combination.pop()
