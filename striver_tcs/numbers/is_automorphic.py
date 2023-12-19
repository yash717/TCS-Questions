# Function to check if a number is an Automorphic number
def is_automorphic(num):
    square = num * num
    # Convert both the number and its square to strings to compare their endings
    num_str = str(num)
    square_str = str(square)

    # Compare the last 'n' digits of the square with the original number
    if square_str[-len(num_str):] == num_str:
        return "Automorphic Number"
    else:
        return "Not an Automorphic Number"


# Test cases
num1 = 76
print(f"Is {num1} an automorphic number? {is_automorphic(num1)}")
# Output: Is 76 an automorphic number? Automorphic Number

num2 = 25
print(f"Is {num2} an automorphic number? {is_automorphic(num2)}")
# Output: Is 25 an automorphic number? Automorphic Number
