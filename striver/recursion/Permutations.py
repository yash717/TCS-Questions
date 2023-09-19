"""
Brute Force Solution:
The brute force approach involves generating all possible permutations of the given distinct integers array nums. This can be achieved using backtracking or recursion to generate all permutations by trying out all possible combinations of elements in the array.

Here's the code with detailed comments explaining each step:"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def generate_permutations(current, remaining, result):
            if not remaining:
                result.append(current[:])
                return

            for i in range(len(remaining)):
                # Add the element to the current permutation
                current.append(remaining[i])
                # Recursive call without the current element
                generate_permutations(
                    current, remaining[:i] + remaining[i+1:], result)
                current.pop()   # Backtrack by removing the last added element

        all_permutations = []
        generate_permutations([], nums, all_permutations)

        return all_permutations


# Example usage:
sol = Solution()
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
print(sol.permute([1, 2, 3]))
print(sol.permute([0, 1]))      # Output: [[0, 1], [1, 0]]
print(sol.permute([1]))         # Output: [[1]]


"""
Optimal Solution:
The optimal solution for this problem involves using backtracking to generate permutations more efficiently. The key insight here is to swap elements in the array to generate permutations while tracking the current index that we're swapping.

Here's the code for the optimal solution with detailed comments:"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first=0):
            # Base case: If the first index reaches the length of the array,
            # a full permutation is formed, so append it to the result.
            if first == len(nums):
                result.append(nums[:])
                return

            # Iterate over remaining elements starting from the 'first' index.
            for i in range(first, len(nums)):
                # Swap the element at index 'first' with the element at index 'i'.
                nums[first], nums[i] = nums[i], nums[first]

                # Recurse to the next index, which is 'first + 1', to generate permutations.
                backtrack(first + 1)

                # Backtrack by swapping elements back to their original state.
                nums[first], nums[i] = nums[i], nums[first]

        result = []  # List to store all permutations
        backtrack()  # Start the backtracking process

        return result  # Return the list of all permutations

