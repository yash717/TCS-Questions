"""
Optimal Approach 2 (Using XOR): 
Using XOR, we are going to solve this problem using the following 3 steps.

Assume the repeating number to be X and the missing number to be Y.

Step 1: Find the XOR of the repeating number(X) and the missing number(Y)
i.e. (X^Y) = (a[0]^a[1]^…..^a[n-1]) ^ (1^2^……..^N)

In order to find the XOR of the repeating number and the missing number, we will first XOR all the array elements and with that value, we will again XOR all the numbers from 1 to N.
(X^Y) = (a[0]^a[1]^…..^a[n-1]) ^ (1^2^3^……..^N)
Step 2: Find the first different bit from right between the repeating and the missing number i.e. the first set bit from right in (X^Y)

By convention, the repeating and the missing number must be different and since they are different they must contain different bits. Now, our task is to find the first different bit from the right i.e. the end. We know, the XOR of two different bits always results in 1. The position of the first different bit from the end will be the first set bit(from the right) in (X^Y) that we have found in step 1.
Step 3: Based on the position of the different bits we will group all the elements ( i.e. all array elements + all elements between 1 to N) into 2 different groups

Assume an imaginary array containing all the array elements and all the elements between 1 to N. Now, we will check that particular position for each element of that imaginary array and then if the bit is 0, we will insert the element into the 1st group otherwise, we will insert it into the 2nd group. 
After performing this step, we will get two groups. Now, if we XOR all the elements of those 2 groups, we will get 2 numbers. One of them will be the repeating number and the other will be the missing number. But until now, we do not know which one is repeating and which one is missing.
Last step: Figure out which one of the numbers is repeating and which one is missing

We will traverse the entire given array and check which one of them appears twice. And the number that appears twice is the repeating number and the other one is the missing number.
Approach:
The steps are as follows:

For the first step, we will run a loop and calculate the XOR of all the array elements and the numbers between 1 to N. Let’s call this value xr.
In order to find the position of the first set bit from the right, we can either use a loop or we can perform AND of the xr and negation of (xr-1) i.e. (xr & ~(xr-1)).
Now, we will take two variables i.e. zero and one. Now, we will check the bit of that position for every element (array elements as well as numbers between 1 to N).
If the bit is 1: We will XOR that element with variable one.
If the bit is 0: We will XOR that element with variable zero.
Finally, we have two variables i.e. two numbers zero and one. Among them, one is repeating and the other is missing. It’s time to identify them. 
We will traverse the entire array and check how many times variable zero appears. 
If it appears twice, it will be the repeating number, otherwise, it will be the missing. Now, based on variable zero’s identity, we can easily identify in which category, variable one belongs."""


from typing import List


def findMissingRepeatingNumbers(a):
    n = len(a)  # size of the array

    xr = 0

    # Step 1: Find XOR of all elements:
    for i in range(n):
        xr = xr ^ a[i]
        xr = xr ^ (i + 1)

    # Step 2: Find the differentiating bit number:
    number = (xr & ~(xr - 1))

    # Step 3: Group the numbers:
    zero = 0
    one = 0
    for i in range(n):
        # part of 1 group:
        if ((a[i] & number) != 0):
            one = one ^ a[i]
        # part of 0 group:
        else:
            zero = zero ^ a[i]

    for i in range(1, n + 1):
        # part of 1 group:
        if ((i & number) != 0):
            one = one ^ i
        # part of 0 group:
        else:
            zero = zero ^ i

    # Last step: Identify the numbers:
    cnt = 0
    for i in range(n):
        if (a[i] == zero):
            cnt += 1

    if (cnt == 2):
        return [zero, one]
    return [one, zero]


if __name__ == '__main__':
    a = [3, 1, 2, 5, 4, 6, 7, 5]
    ans = findMissingRepeatingNumbers(a)
    print(
        "The repeating and missing numbers are: {", ans[0], ", ", ans[1], "}\n")


"""
The given code is used to find the missing number (M) and the repeating number (R) in an array arr of size n.

Here's a step-by-step explanation of the code:

Step 1:

Initialize xor to 0. This variable will be used to calculate the XOR of all elements in arr and the numbers from 1 to n.
Calculate xor by performing XOR between xor and each element arr[i] in the array, as well as each number i from 1 to n. This is done to obtain the XOR of all elements and numbers.
The variable rightmost_set_bit is calculated by performing a bitwise AND operation between xor and its two's complement -xor. It helps in identifying the differing bit position between the missing number and the repeating number.
Step 2:

Initialize repeating to 0. This variable will be used to calculate the repeating number (R).
Iterate through arr and check if the rightmost_set_bit is set in each element. If it is, perform XOR with repeating to find the repeating number. This is done because all other numbers have cancelled out in the XOR operation.
Similarly, iterate through the numbers from 1 to n and check if the rightmost_set_bit is set. If it is, perform XOR with repeating to find the repeating number.
Step 3:

Calculate the missing number (M) by performing XOR between xor and repeating.
Return a tuple (missing, repeating) containing the missing number and the repeating number.
The code uses the concept of XOR to find the missing and repeating numbers. By performing XOR operations, the differing bits between the missing and repeating numbers are identified, allowing us to isolate them and obtain the desired results.
"""


def missingAndRepeating(arr, n):
    # Step 1: Find the repeating number (R) using the concept of XOR
    xor = 0
    for i in range(n):
        xor ^= arr[i]
    for i in range(1, n+1):
        xor ^= i
    rightmost_set_bit = xor & -xor
    repeating = 0
    for i in range(n):
        if arr[i] & rightmost_set_bit != 0:
            repeating ^= arr[i]
    for i in range(1, n+1):
        if i & rightmost_set_bit != 0:
            repeating ^= i

    # Step 2: Find the missing number (M) using the concept of XOR
    missing = xor ^ repeating

    # Step 3: Return the pair (M, R)
    return (missing, repeating)
