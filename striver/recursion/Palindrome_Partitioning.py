"""PROBLEM STATEMENT"""

"""Problem Statement: You are given a string s, partition it in such a way that every substring is a palindrome.
Return all such palindromic partitions of s."""


"""EXPLANATION"""
"""In this problem, you are given a string s.
The task is to partition s into substrings such that each substring is a palindrome.
A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.

You need to find all possible palindrome partitioning of the string s and return them as a list of lists.

Here are a few examples to help you understand the problem:

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Explanation:
There are two possible ways to partition the string "aab" into palindromes:

["a","a","b"]: Here, "a", "a", and "b" are all palindromes.
["aa","b"]: Here, "aa" and "b" are palindromes."""

"""STRIVER CODE"""




import json  # Importing the 'json' module
from sys import stdin  # Importing the 'stdin' module from 'sys'
from math import *  # Importing all modules from the 'math' package
from collections import *  # Importing all modules from the 'collections' package
from sys import *  # Importing all modules from the 'sys' package
from os import *  # Importing all modules from the 'os' package
from typing import List
class Solution:
    """
    This class defines the solution to the partition problem.
    """

    def partition(self, s: str) -> List[List[str]]:
        """
        This function partitions the given string into a list of palindromes.

        Args:
            s: The string to be partitioned.

        Returns:
            A list of lists of strings, where each inner list represents a palindrome.
        """

        # Initialize the result list.
        res = []

        # Initialize the path list.
        path = []

        # Recursively search for partitions.
        def partitionHelper(index: int):
            # Base case.
            if index == len(s):
                # Add the current path to the result list.
                res.append(path[:])
                return

            # Iterate over all possible substrings starting at the current index.
            for i in range(index, len(s)):
                # Check if the substring is a palindrome.
                if isPalindrome(s, index, i):
                    # Add the substring to the path.
                    path.append(s[index:i + 1])

                    # Recursively search for partitions of the remaining substring.
                    partitionHelper(i + 1)

                    # Remove the substring from the path.
                    path.pop()

        # Recursively search for partitions of the entire string.
        partitionHelper(0)

        # Return the result list.
        return res


def isPalindrome(s: str, start: int, end: int) -> bool:
    """
    This function checks if the given substring is a palindrome.

    Args:
        s: The substring to be checked.
        start: The start index of the substring.
        end: The end index of the substring.

    Returns:
        True if the substring is a palindrome, False otherwise.
    """

    # Iterate over the substring from the start to the end.
    while start <= end:
        # If the characters at the start and end indices are not equal, the substring is not a palindrome.
        if s[start] != s[end]:
            return False

        # Increment the start index and decrement the end index.
        start += 1
        end -= 1

    # The substring is a palindrome.
    return True


""""LEETCODE SOLUTION"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []  # List to store the resulting partitions
        path = []  # Current path of palindromic substrings

        # Recursive helper function to generate partitions
        def partitionHelper(index: int):
            # If index reaches the end of the string, a valid partition is found
            if index == len(s):
                res.append(path[:])  # Add the current path to the result list
                return

            # Iterate over the string starting from the current index
            for i in range(index, len(s)):
                # If the substring from index to i is a palindrome
                if self.isPalindrome(s, index, i):
                    path.append(s[index:i + 1])  # Add it to the current path
                    # Recursively call the helper function with the next index
                    partitionHelper(i + 1)
                    path.pop()  # Backtrack by removing the last added palindrome from the path

        # Function to check if a substring is a palindrome
        def isPalindrome(self, s: str, start: int, end: int) -> bool:
            while start <= end:  # Compare characters from start and end, moving inward
                if s[start] != s[end]:  # If characters do not match, it's not a palindrome
                    return False
                start += 1  # Move start index forward
                end -= 1  # Move end index backward
            return True  # If the loop completes, it's a palindrome

        # Call the helper function to generate partitions starting from index 0
        partitionHelper(0)
        return res  # Return the resulting partitions


"""CODING NINJA CODE"""

from os import *  # Importing all modules from the 'os' package
from sys import *  # Importing all modules from the 'sys' package
from collections import *  # Importing all modules from the 'collections' package
from math import *  # Importing all modules from the 'math' package

from sys import stdin  # Importing the 'stdin' module from 'sys'
import json  # Importing the 'json' module

def partition(s):
    res = []  # List to store the resulting partitions
    path = []  # List to store the current partition path

    # Helper function to generate all possible partitions
    def partitionHelper(index: int):
        # Base case: If we have reached the end of the string,
        # add the current partition path to the result list
        if index == len(s):
            res.append(path[:])
            return

        # Iterate over the string starting from the current index
        for i in range(index, len(s)):
            # If the substring from the current index to 'i' is a palindrome,
            # add it to the current partition path and recursively call the function
            if isPalindrome(s, index, i):
                path.append(s[index:i + 1])
                partitionHelper(i + 1)
                path.pop()  # Backtrack by removing the last added palindrome

    # Helper function to check if a substring is a palindrome
    def isPalindrome(s: str, start: int, end: int) -> bool:
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    # Start the partitioning process from the beginning of the string
    partitionHelper(0)
    return res  # Return the resulting partitions


s = stdin.readline().rstrip()  # Read the input string from standard input and remove the trailing newline character

final = partition(s)  # Call the partition function to get the resulting partitions

for ele in final:
    ele = sorted(ele)  # Sort the elements of each partition in lexicographical order
    print(json.dumps(ele))  # Print the partition as a JSON-formatted string
