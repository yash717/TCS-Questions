def sum_in_range(l1, l2):
    total_sum = 0
    for i in range(l1, l2+1):
        total_sum += i
    return total_sum


# Test cases
l1, r1 = 2, 7
print("Sum of numbers from", l1, "to", r1, "is:", sum_in_range(
    l1, r1))  # Output: Sum of numbers from 2 to 7 is: 27

l2, r2 = 5, 9
print("Sum of numbers from", l2, "to", r2, "is:", sum_in_range(
    l2, r2))  # Output: Sum of numbers from 5 to 9 is: 35
