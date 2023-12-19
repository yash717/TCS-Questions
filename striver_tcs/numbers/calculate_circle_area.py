# Function to calculate the area of a circle
def calculate_circle_area(radius):
    # π value is considered as 3.14
    pi = 3.14
    # Formula to calculate the area of a circle: πr^2
    area = pi * radius ** 2
    return area


# Test cases
radius1 = 5
print("Area of the circle with radius 5:",
      calculate_circle_area(radius1))  # Output: 78.5

radius2 = 4
print("Area of the circle with radius 4:",
      calculate_circle_area(radius2))  # Output: 50.24
