count = 'y'
while count.lower() == 'y':

    num_1 = input('Enter first number ')
    num_2 = input('Enter second number ')
    calc_option = input('Choose operation, please ')

    if calc_option == '+':
        if num_1.isdigit() and num_2.isdigit():
            result = int(num_1) + int(num_2)
        else:
            result = float(num_1) + float(num_2)
    elif calc_option == '-':
        if num_1.isdigit() and num_2.isdigit():
            result = int(num_1) - int(num_2)
        else:
            result = float(num_1) - float(num_2)
    elif calc_option == '*':
        if num_1.isdigit() and num_2.isdigit():
            result = int(num_1) * int(num_2)
        else:
            result = float(num_1) * float(num_2)
    elif calc_option == '/':
        if num_1.isdigit() and num_2.isdigit():
            result = int(num_1) / int(num_2)
        else:
            result = float(num_1) / float(num_2)
    elif calc_option == '**':
        if num_1.isdigit() and num_2.isdigit():
            result = int(num_1) ** int(num_2)
        else:
            result = float(num_1) ** float(num_2)
    else:
        print('Wrong operation. You can try only +, -, *, /, **')

    print(result)

    count = input('Should we continue? y/n: ')
    if count == 'n':
        break
