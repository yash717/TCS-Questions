"""problem statement"""

"""The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

 

Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
Example 3:

Input: n = 3, k = 1
Output: "123"
 

Constraints:

1 <= n <= 9
1 <= k <= n!
"""

"""problem statement explanation"""
"""Sure! The problem asks us to find the kth permutation sequence of the set [1, 2, 3, ..., n]. 

Let's break down the problem statement step by step:

1. The set [1, 2, 3, ..., n] represents all the numbers from 1 to n. For example, if n = 3, the set would be [1, 2, 3].

2. By listing and labeling all of the permutations in order, we generate a sequence of permutations. For example, when n = 3, the sequence is:

   - "123"
   - "132"
   - "213"
   - "231"
   - "312"
   - "321"

   Each permutation is a unique arrangement of the numbers in the set.

3. We are given two inputs: n and k. n represents the size of the set, and k represents the position of the permutation we want to find.

4. The task is to return the kth permutation sequence. For example, if n = 3 and k = 3, the expected output is "213". If n = 4 and k = 9, the expected output is "2314".

5. The constraints state that n is between 1 and 9 (inclusive), and k is between 1 and n! (n factorial).

To solve this problem, we can use a mathematical approach that leverages the concept of factorials. By calculating the factorials of the numbers from 1 to n, we can determine the digit at each position in the kth permutation sequence."""


"""striver's code"""


from typing import List
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = 1  # Variable to store the factorial value
        numbers = []  # List to store the numbers used for permutation

        # Calculate the factorial and store the numbers
        for i in range(1, n):
            fact *= i
            numbers.append(i)
        numbers.append(n)

        ans = ""  # Variable to store the resulting permutation sequence
        k -= 1  # Adjust k to match 0-based indexing

        # Generate the permutation sequence
        while True:
            # Append the digit at the current index to the sequence
            ans += str(numbers[k // fact])
            numbers.pop(k // fact)  # Remove the used digit from the list

            if not numbers:
                break  # If there are no more numbers, exit the loop

            k %= fact  # Update k to the remaining value
            fact //= len(numbers)  # Update the factorial value

        return ans  # Return the resulting permutation sequence


if __name__ == "__main__":
    n = 3  # Given n value
    k = 3  # Given k value

    obj = Solution()  # Create an instance of the Solution class
    # Call the getPermutation method to get the kth permutation
    ans = obj.getPermutation(n, k)
    # Print the resulting permutation sequence
    print("The Kth permutation sequence is", ans)
