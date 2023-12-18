def relativeSortArray(P, Q):
    # Count occurrences of elements in P
    count = {}
    for num in P:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    # Create a list to store the result
    result = []

    # Process elements in Q
    for val in Q:
        if val in count:
            result.extend([val] * count[val])
            count[val] = 0

    # Append remaining elements in sorted order
    for key in sorted(count.keys()):
        if count[key] > 0:
            result.extend([key] * count[key])

    return result


# Test cases
P1 = [20, 10, 20, 50, 70, 10, 90, 30, 60, 80, 80]
Q1 = [20, 10, 80, 30]
result1 = relativeSortArray(P1, Q1)
print("Output for Example 1:", result1)

P2 = [20, 10, 20, 50, 70, 10, 90, 30, 60, 80, 80]
Q2 = [99, 22, 444, 56]
result2 = relativeSortArray(P2, Q2)
print("Output for Example 2:", result2)
