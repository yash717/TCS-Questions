# Function to calculate the factorial of a number
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        fact = 1
        for i in range(2, num + 1):
            fact *= i
        return fact

# Function to check if a number is a strong number


def is_strong_number(n):
    original_num = n
    # Initialize sum to store the sum of factorial of individual digits
    sum_factorial = 0
    # Calculate factorial of individual digits and sum them up
    while n > 0:
        digit = n % 10
        sum_factorial += factorial(digit)
        n //= 10

    # Check if the sum of factorial of digits is equal to the original number
    if sum_factorial == original_num:
        return "Yes"
    else:
        return "No"


# Test cases
num1 = 145
# Output: Is 145 a strong number? Yes
print(f"Is {num1} a strong number? {is_strong_number(num1)}")

num2 = 26
# Output: Is 26 a strong number? No
print(f"Is {num2} a strong number? {is_strong_number(num2)}")
