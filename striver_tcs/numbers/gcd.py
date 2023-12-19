def gcd(num1, num2):
    # Initialize gcd as 1 (to handle case where no common divisor found)
    gcd = 1

    # Loop through numbers from 1 to the minimum of num1 and num2
    for i in range(1, min(num1, num2) + 1):
        # Check if both num1 and num2 are divisible by the current number i
        if num1 % i == 0 and num2 % i == 0:
            # If yes, update gcd with the current number i
            gcd = i

    # Return the greatest common divisor found
    return gcd


if __name__ == "__main__":
    # Define two numbers for which GCD needs to be found
    num1 = 12
    num2 = 4

    # Call the gcd function and store the result
    result = gcd(num1, num2)

    # Display the GCD of the two numbers
    print("The GCD of the two numbers is:", result)
