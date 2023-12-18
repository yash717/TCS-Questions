def check_positive_negative(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"


# Test cases
num1 = 5
print(f"Input: n={num1}")
print(f"Output: {check_positive_negative(num1)}")
# Output: Positive

num2 = -6
print(f"\nInput: n={num2}")
print(f"Output: {check_positive_negative(num2)}")
# Output: Negative
