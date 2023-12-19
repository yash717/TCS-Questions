def find_roots(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Case 1: If discriminant is positive, roots are real and different
    if discriminant > 0:
        root1 = (-b + (discriminant**0.5)) / (2*a)
        root2 = (-b - (discriminant**0.5)) / (2*a)
        print(f"Roots are real and different, i.e ({root1}, {root2})")

    # Case 2: If discriminant is zero, roots are real and equal
    elif discriminant == 0:
        root = -b / (2*a)
        print(f"Roots are real and equal, i.e ({root}, {root})")

    # Case 3: If discriminant is negative, roots are complex
    else:
        real_part = -b / (2*a)
        imaginary_part = (-discriminant)**0.5 / (2*a)
        print(
            f"Roots are complex, i.e ({real_part}+{imaginary_part}i, {real_part}-{imaginary_part}i)")


# Test cases
find_roots(1, -3, -10)  # Output: Roots are real and different, i.e (5.0, -2.0)
# Output: Roots are complex, i.e (-0.5+1.732i, -0.5-1.732i)
find_roots(1, 1, 1)
