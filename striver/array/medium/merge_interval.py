"""
The given problem asks us to merge overlapping intervals in an array arr and return a new array of non-overlapping intervals. We need to sort the intervals based on the starting point and merge the overlapping intervals.

To solve this problem, we can use the following approach:

Sort the intervals based on the starting point in increasing order. This ensures that overlapping intervals are adjacent after sorting.

Initialize an empty list result to store the merged intervals.

Iterate through the sorted intervals:

If result is empty or the current interval does not overlap with the last interval in result, add the current interval to result.
Otherwise, the current interval overlaps with the last interval in result. Merge the intervals by updating the ending point of the last interval in result to the maximum of the ending points of both intervals.
After the iteration, result will contain the merged non-overlapping intervals.

Here's the code that implements the above steps with detailed comments:
"""

from typing import *


def mergeOverlappingIntervals(arr: List[List[int]]) -> List[List[int]]:
    # Step 1: Sort the intervals based on the starting point in increasing order
    arr.sort(key=lambda x: x[0])

    # Step 2: Initialize an empty list to store the merged intervals
    result = []

    # Step 3: Iterate through the sorted intervals
    for interval in arr:
        # Check if result is empty or the current interval does not overlap with the last interval in result
        if not result or interval[0] > result[-1][1]:
            result.append(interval)
        else:
            # Merge the intervals by updating the ending point of the last interval in result
            result[-1][1] = max(result[-1][1], interval[1])

    # Step 4: Return the merged non-overlapping intervals
    return result


"""


This code defines a function mergeOverlappingIntervals that takes an array arr of intervals as input. 
It follows the steps described above to merge the overlapping intervals and returns the resulting 
array of non-overlapping intervals.

Note: The code assumes that arr is a list of intervals where each interval
is represented by a list [L, R] with the starting point L and ending point R.
"""
