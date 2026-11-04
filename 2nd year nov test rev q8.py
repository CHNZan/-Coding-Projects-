num_1 = int(input('Enter a number: '))
num_2 = int(input('Enter a 2nd number: '))
num_3 = int(input('Enter a 3rd number: '))

if num_1 + num_2 == num_3 or num_2 + num_3 == num_1 or num_1 + num_3 == num_2:
    print('2 of the input numbers are a sum of the other')
else:
    pass