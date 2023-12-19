def CalculatePower(N, X):
    power = 1
    for i in range(1, X+1):
        power *= N
    return (N, X, power)


N, X = 2, 3
print(CalculatePower(N, X))  # Output: 8

N, X = 3, 4
print(CalculatePower(N, X))  # Output: 81
