def solve(str):
    result = ""
    for i in str:
        ascii_val = ord(i)
        if (65 <= ascii_val <= 91) or (97 <= ascii_val <= 122):
            result += i
    return result


# Test case
input_str = "take12% *&u ^$#forward"
print("Resultant string:")
print(solve(input_str))
