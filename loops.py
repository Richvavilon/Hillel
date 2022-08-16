user = input('Enter something ')

upper_letters = ''
collector_spaces = ''
volwes_letters = ''
counter = 0

for index, element in enumerate(user):

    if element.isupper():
        upper_letters += element

    if element == ' ':
        collector_spaces += str(index) + ','

    if element.lower() in 'a e i o u':
        volwes_letters += element

    if element.isdigit():
        counter += 1
        if counter == 3:
            print('Too many numbers')
            break
    else:
        counter = 0
if counter != 3:
    print('Correct end')

print(upper_letters)
print(collector_spaces)
print(volwes_letters)
