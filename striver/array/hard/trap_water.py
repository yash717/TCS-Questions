# brute force
class Solution(object):
    def trap(self, height):
        n = len(height)
        trapped_water = 0

        for i in range(n):
            left_max = 0
            right_max = 0

            # Find the maximum height on the left side of the current index
            for j in range(i):
                left_max = max(left_max, height[j])

            # Find the maximum height on the right side of the current index
            for j in range(i + 1, n):
                right_max = max(right_max, height[j])

            # Calculate the trapped water at the current index
            trapped_water += max(0, min(left_max, right_max) - height[i])

        return trapped_water

# optimal solution


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left = 0
        right = n - 1
        left_max = 0
        right_max = 0
        trapped_water = 0

        while left < right:
            # Calculate trapped water at the left index
            if height[left] < height[right]:
                # If height[left] is smaller than height[right],
                # the trapped water at the left index depends on the left_max
                # because there is a potential for trapping water on the left side.
                left_max = max(left_max, height[left])
                trapped_water += left_max - height[left]
                left += 1
            else:
                # Calculate trapped water at the right index
                # If height[left] is greater than or equal to height[right],
                # the trapped water at the right index depends on the right_max
                # because there is a potential for trapping water on the right side.
                right_max = max(right_max, height[right])
                trapped_water += right_max - height[right]
                right -= 1

        return trapped_water


"""
Explanation and Comments:

We start by initializing two pointers, left and right, to the first and last indices of the array, respectively.
We also initialize two variables, left_max and right_max, to keep track of the maximum height on the left and right sides as we traverse the array.
We initialize trapped_water to 0, which will store the total trapped water.
We use a while loop to iterate until left is less than right, meaning there are still elements to consider.
Inside the while loop, we check the heights at indices left and right.
If the height at left is smaller than the height at right, it means there is a potential for trapping water on the left side. So, we calculate the trapped water at the left index by subtracting the height at left from the left_max. Then, we move the left pointer to the right (i.e., left += 1) to consider the next index.
If the height at left is greater than or equal to the height at right, it means there is a potential for trapping water on the right side. So, we calculate the trapped water at the right index by subtracting the height at right from the right_max. Then, we move the right pointer to the left (i.e., right -= 1) to consider the next index.
We continue this process until the left and right pointers meet (i.e., left >= right), which indicates that we have considered all elements in the array.
Finally, we return the total trapped water.
"""
