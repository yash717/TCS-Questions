"""PROBLEM STATEMENT"""
"""Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.
The test cases are generated such that the number
of unique combinations that sum up to target is less than 150 combinations for the given input.


Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations."""

"""EXPLANATION OF THE PROBLEM STATEMENT"""

"""The problem is asking for a solution that returns all unique combinations of integers from a given array,
where the chosen numbers sum up to a given target.
The same number from the array can be chosen multiple times to form a combination.
For example, if the given array is [2, 3, 6, 7] and the target is 7, the expected output is [[2, 2, 3], [7]].
In this case, the combinations [2, 2, 3] and [7] are the only two unique combinations that sum up 
to the target value of 7.
To solve this problem, we can use a backtracking approach. Here's a general outline of the algorithm:
Define a recursive function that takes parameters: the current combination,
the current sum, and the index of the current candidate.
Inside the function:
Check if the current sum equals the target. If it does, add the current combination to the result.
If the current sum exceeds the target, stop exploring further.
Iterate over the candidates starting from the current index:
Add the current candidate to the current combination.
Recursively call the function with the updated combination, the updated sum (increased by the current candidate),
and the same index.
Remove the last added candidate from the combination (backtrack).
Start the recursive function with an empty combination, a sum of 0, and the index of the first candidate.
Return the result containing all unique combinations.
By following this approach, we can generate all unique combinations that sum up to the target value.
The backtracking technique allows us to explore different possibilities and efficiently find all valid combinations."""


"""LEETCODE SOLUTION"""


class Solution:
    def combinationSum(self, candidates, target):
        # Initialize an empty list to store the combinations
        combinations = []
        # Call the recursive function to generate the combinations
        self.generate_sum(candidates, target, [], combinations)
        # Return the generated combinations
        return combinations

    def generate_sum(self, candidates, target, curr_combinations, combinations):
        # If the target sum is reached, add the current combination to the list of combinations
        if target == 0:
            combinations.append(curr_combinations[:])

        # If the target sum is negative, return (backtrack)
        if target < 0:
            return

        # Iterate over the candidates
        for i in range(len(candidates)):
            # Add the current candidate to the current combination
            curr_combinations.append(candidates[i])
            # Recursively call the function with the remaining candidates and updated target
            self.generate_sum(
                candidates[i:], target - candidates[i], curr_combinations, combinations)
            # Remove the last added candidate (backtrack)
            curr_combinations.pop()


# Create an instance of the Solution class
sol = Solution()

# Define the input candidates and target
candidates = [2, 3, 6, 7]
target = 7

# Call the combinationSum function
result = sol.combinationSum(candidates, target)

# Print the result
print(result)


"""CODING NINJA SOLUTION"""


def findSubsetsThatSumToK(arr, n, k):
    combinations = []
    generate_combinations(arr, n, k, 0, [], combinations)
    return combinations


def generate_combinations(arr, n, k, index, curr_combinations, combinations):
    # Base case: If we have processed all elements in the array
    if index == n:
        # Check if the current subset sum equals k
        if sum(curr_combinations) == k:
            # Add the current subset to the list of combinations
            combinations.append(curr_combinations[:])
        return

    # Include the current element in the subset
    generate_combinations(arr, n, k, index + 1,
                          curr_combinations + [arr[index]], combinations)

    # Exclude the current element from the subset
    generate_combinations(arr, n, k, index + 1,
                          curr_combinations, combinations)
