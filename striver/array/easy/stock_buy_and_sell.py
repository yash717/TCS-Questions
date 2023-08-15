"""
The given problem asks us to maximize our profit by buying and selling a stock on different days. We need to find the maximum profit we can achieve from this transaction.

To solve this problem, we can use a simple approach that involves keeping track of the minimum price seen so far and updating the maximum profit whenever we find a higher selling price.

Here's a step-by-step explanation of the approach:

Initialize two variables: min_price and max_profit.

min_price will track the minimum price seen so far.
max_profit will track the maximum profit we can achieve.
Iterate through the prices array:

Update min_price to the minimum value between the current price and min_price.
Update max_profit to the maximum value between the difference of the current price and min_price and max_profit.
After the iteration, max_profit will hold the maximum profit we can achieve.

Here's the code that implements the above steps with detailed comments:"""


class Solution(object):
    def maxProfit(self, prices):
        # Step 1: Initialize variables
        min_price = float('inf')  # Initialize min_price with positive infinity
        max_profit = 0  # Initialize max_profit to 0

        # Step 2: Iterate through the prices array
        for price in prices:
            # Update min_price and max_profit
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        # Step 3: Return the maximum profit
        return max_profit


"""This code defines a class Solution with a method maxProfit that takes an array prices as input. It follows the steps described above to find the maximum profit from buying and selling the stock.

Note: The code assumes that prices is a list of integers representing the prices of the stock on different days, and the length of prices is within the given constraints."""


"""ALTERNATE CODE"""


class Solution:
    def maxProfit(self, prices):
        left = 0  # Buy
        right = 1  # Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left]  # our current Profit
            if prices[left] < prices[right]:
                max_profit = max(currentProfit, max_profit)
            else:
                left = right
            right += 1

        return max_profit


"""
The code defines a class Solution with a method maxProfit that takes an array prices as input.
It initializes variables left and right to keep track of the indices for buying and selling, respectively.
max_profit is initialized to 0 to store the maximum profit.

The code enters a while loop to iterate through the prices array.
It calculates the currentProfit as the difference between the price at right (sell) and the price at left (buy).
If the price at left is less than the price at right, it means a potential profit can be made.
It updates max_profit to the maximum value between currentProfit and the current max_profit.
If the price at left is not less than the price at right, it means a better buying opportunity is found.
It updates left to right, indicating a new buying position.
It increments right to move to the next day for potential selling.


The code enters a while loop to iterate through the prices array.
It calculates the currentProfit as the difference between the price at right (sell) and the price at left (buy).
If the price at left is less than the price at right, it means a potential profit can be made.
It updates max_profit to the maximum value between currentProfit and the current max_profit.
If the price at left is not less than the price at right, it means a better buying opportunity is found.
It updates left to right, indicating a new buying position.
It increments right to move to the next day for potential selling."""
