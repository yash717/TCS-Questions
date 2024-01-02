def remove_brackets(str):
    f_str = ""
    for i in str:
        if i != "(" and i != ")":
            f_str += i
    return f_str


expression_1 = "a+((b-c)+d)"
expression_2 = "(((a-b))+c)"

print("Input:", expression_1)
print("Output:", remove_brackets(expression_1))

print("Input:", expression_2)
print("Output:", remove_brackets(expression_2))
