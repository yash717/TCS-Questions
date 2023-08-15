
def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    # Base case: if n is 0, return 1
    if n == 0:
        return 1.0

    # If n is negative, convert x to 1/x and change n to its absolute value
    if n < 0:
        x = 1 / x
        n = abs(n)

    # Recursive call to calculate x^(n/2)
    half = myPow(x, n // 2)

    # Check if n is even
    if n % 2 == 0:
        return half * half
    else:
        return half * half * x


if __name__ == "__main__":
    print(myPow(2, 10))


"""
In this code, the myPow function takes x (a float) and n (an integer) as input and returns the result as a float.

Here's a step-by-step explanation of the code:

The base case is when n is 0. In this case, we return 1.0 since any number raised to the power of 0 is 1.

If n is negative, we convert x to its reciprocal (1/x) and change n to its absolute value. This is done to handle negative exponents.

We recursively calculate half by calling myPow with x and n // 2. This step computes x^(n/2).

If n is even, we return half * half since x^n can be computed as (x^(n/2))^2.

If n is odd, we return half * half * x since x^n can be computed as (x^(n/2))^2 * x.

By using recursion and dividing the exponent by 2 at each step, we can calculate the power efficiently. This approach has a time complexity of O(log n), as we divide the problem size in half at each recursive step.



 """
