def is_harshad_number(num):
    strn_num = str(num)
    digit_sum = 0
    for i in strn_num:
        digit_sum += int(i)

    if num % digit_sum == 0:
        return True
    else:
        return False


# Test cases
num1 = 378
if is_harshad_number(num1):
    print(f"{num1} is a Harshad number.")
else:
    print(f"{num1} is not a Harshad number.")

num2 = 379
if is_harshad_number(num2):
    print(f"{num2} is a Harshad number.")
else:
    print(f"{num2} is not a Harshad number.")
