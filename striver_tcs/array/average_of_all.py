def average(nums):
    sum = 0
    n = len(nums)
    for i in nums:
        sum += i
    average = sum/n
    return average


a = [1, 2, 3, 4, 5]
print(average(a))
