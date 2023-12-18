def check_even_odd(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"


# Test cases
num1 = 5
print(f"Input: n={num1}")
print(f"Output: {check_even_odd(num1)}")
# Output: odd

num2 = 6
print(f"\nInput: n={num2}")
print(f"Output: {check_even_odd(num2)}")
# Output: even
