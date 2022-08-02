a = 3 != 5

b = 5 == 5
b_1 = 5 >= 5
b_2 = 5 <= 5
b_3 = bool(5 + 5)
b_4 = bool(5 / 5)

c = 3 < 4 != False  # Am I wrong here?

line_1 = True or True and False
line_2 = True and True and not False
line_3 = not True or True or False
line_4 = True or True or False
line_5 = not True or (True or False)

x = bool(None)
x_1 = 7
result = x == x_1

empty_str = bool('')
example = 10 - 1
result_2 = empty_str == example

print(a, b, b_1, b_2, b_3, b_4, c, line_1, line_2, line_3, line_4, line_5, result, result_2, sep='\n')
