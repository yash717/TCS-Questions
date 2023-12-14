def insertBeginning(array, x):
    array.insert(0, x)


def insertEnding(array, x):
    array.append(x)


def insertAtPos(array, x, p):
    array.insert(p, x)


# Given array
array = [1, 2, 3, 4, 5]
print("Original Array:", array)

# Inserting elements
insertBeginning(array, 6)
insertEnding(array, 7)
insertAtPos(array, 8, 4)

# Displaying the modified array
print("Modified Array:", array)
