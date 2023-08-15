"""
In this combinatorics solution, we can calculate the number of unique paths using the concept of combinations.

To reach the bottom-right corner, the robot needs to move down m - 1 steps and move right n - 1 steps. The total number of steps required to reach the target cell is m + n - 2.

We can calculate the number of unique paths by calculating the combination of total_steps choose down_steps, which is denoted as C(total_steps, down_steps). This represents the number of ways to choose down_steps steps out of total_steps steps.

Using the formula for combinations, we can iterate from 1 to down_steps and calculate the combination value incrementally.

Finally, we return the calculated paths as the total number of unique paths.

The combinatorics solution provides an efficient way to calculate the number of paths without explicitly calculating all possible paths. It has a time complexity of O(min(m, n)).
"""


class Solution:
    def uniquePaths(self, m, n):
        # Calculate the total number of steps required to reach the target cell
        total_steps = m + n - 2

        # Calculate the number of steps to move vertically (down) and horizontally (right)
        down_steps = m - 1
        right_steps = n - 1

        # Calculate the combination using the formula C(total_steps, down_steps)
        paths = 1
        for i in range(1, down_steps + 1):
            paths = paths * (total_steps - down_steps + i) // i

        return paths


if __name__ == '__main__':
    obj = Solution()
    paths = obj.uniquePaths(3, 7)
    print("Total paths:", paths)
