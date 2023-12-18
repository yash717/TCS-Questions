# Function to check if a number is prime or not
def is_prime(num):
    # 0 and 1 are not prime numbers
    if num <= 1:
        return False
    # 2 is a prime number
    elif num == 2:
        return True
    else:
        # Check divisibility from 2 to the square root of the number
        for i in range(2, int(num**0.5) + 1):
            # If the number is divisible by any number within this range, it's not prime
            if num % i == 0:
                return False
        # If the number is not divisible by any number within the range, it's prime
        return True


# Test Cases
num1 = 3
if is_prime(num1):
    print(f"{num1} is Prime")
else:
    print(f"{num1} is Non-Prime")

num2 = 26
if is_prime(num2):
    print(f"{num2} is Prime")
else:
    print(f"{num2} is Non-Prime")
