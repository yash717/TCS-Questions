def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_in_range(a, b):
    list = []
    for i in range(a, b+1):
        if is_prime(i) == True:
            list.append(i)
    return list


# Test cases
a, b = 2, 10
print("Prime numbers between", a, "and", b, "are:", prime_in_range(a, b))

a, b = 10, 19
print("Prime numbers between", a, "and", b, "are:", prime_in_range(a, b))
