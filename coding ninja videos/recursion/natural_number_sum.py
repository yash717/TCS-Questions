def sum_n(n):
    if n == 0:
        return 0
    smallOutput = sum_n(n-1)
    output = smallOutput+n
    return output


def factorial(n):
    if n == 0:
        return 1
    smallOutput = factorial(n-1)
    a = n*smallOutput
    return a


n = int(input("Enter number:"))
print(f"factorial of {n}  is : {factorial(n)}")
print(f"sum of {n} natural numbers is :{sum_n(n)}")
