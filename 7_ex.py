num = input('Enter a number:')
while not num.isdigit():
    num = input('Error. Try again. Enter a number:')
print('Entered integer number:', num)
