def remove_space(str):
    const = ""
    for i in str:
        if i != " ":
            const += i
    return const


# Test cases
input_str_1 = "take u forward"
print(f"Input string: {input_str_1}, Output: {remove_space(input_str_1)}")

input_str_2 = "I am very happy today"
print(f"Input string: {input_str_2}, Output: {remove_space(input_str_2)}")
