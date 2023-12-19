def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def express_as_sum_of_two_primes(n):
    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            return True
    return False


# Test cases
num1 = 74
print(express_as_sum_of_two_primes(num1))  # Output: True

num2 = 11
print(express_as_sum_of_two_primes(num2))  # Output: False
