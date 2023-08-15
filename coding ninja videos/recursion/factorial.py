def factorial(n):
    if (n == 0):
        return 1
    else:
        return n*factorial(n-1)


n = int(input("Enter number:"))
print("Factorial:")
print(factorial(n))

''' recursrion is bascially calling itself but here is the catch we use it when we have to pass smaller value and smaller calculation'''


