'''geeks for geeks solution'''


class Solution:
    def subsetSums(self, arr, N):
        subset_sums = []  # Initialize an empty list to store subset sums
        # Call the recursive helper function
        self.generate_subset_sums(arr, N, 0, 0, subset_sums)
        return subset_sums  # Return the subset sums list

    def generate_subset_sums(self, arr, N, index, curr_sum, subset_sums):
        if index == N:  # Base case: If index reaches N, all elements have been considered
            # Append the current sum to the subset sums list
            subset_sums.append(curr_sum)
            return  # Return from the current recursive call

        # Include the current element in the sum
        self.generate_subset_sums(
            arr, N, index + 1, curr_sum + arr[index], subset_sums)

        # Exclude the current element from the sum
        self.generate_subset_sums(arr, N, index + 1, curr_sum, subset_sums)


'''coding ninja solution'''


def subsetSum(nums):
    subset_1 = []
    generate_sums(nums, 0, 0, subset_1)
    subset_1.sort()
    return subset_1


def generate_sums(nums, index, curr_sum, subset_1):
    if index == len(nums):
        subset_1.append(curr_sum)
        return

    generate_sums(nums, index+1, curr_sum+nums[index], subset_1)
    generate_sums(nums, index+1, curr_sum, subset_1)
