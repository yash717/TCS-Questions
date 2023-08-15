class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        count1, count2 = 0, 0
        candidate1, candidate2 = None, None

        # Step 1: Find the potential majority elements
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        # Step 2: Count the occurrences of potential majority elements
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1

        result = []
        if count1 > n // 3:
            result.append(candidate1)
        if count2 > n // 3:
            result.append(candidate2)

        return result


if __name__ == '__main__':
    nums = [11, 33, 33, 11, 33, 11, 11]
    solution = Solution()
    result = solution.majorityElement(nums)
    print("The majority elements are: ", end="")
    for it in result:
        print(it, end=" ")
    print()

"""
This problem requires finding all elements in an array that appear more than ⌊ n/3 ⌋ times. We can solve this problem using a modified version of the Boyer-Moore Majority Vote algorithm.

The algorithm works as follows:

Initialize two variables count1 and count2 to keep track of the counts of two potential majority elements.
Initialize two variables candidate1 and candidate2 to store the potential majority elements.
Iterate through the array nums:
If the current element is equal to candidate1, increment count1 by 1.
If the current element is equal to candidate2, increment count2 by 1.
If count1 is 0, assign the current element to candidate1 and set count1 to 1.
If count2 is 0, assign the current element to candidate2 and set count2 to 1.
If the current element is different from both candidate1 and candidate2, decrement both count1 and count2 by 1.
Reset count1 and count2 to 0.
Iterate through the array again and count the occurrences of candidate1 and candidate2 to determine if they appear more than ⌊ n/3 ⌋ times.
Return the elements that appear more than ⌊ n/3 ⌋ times."""
