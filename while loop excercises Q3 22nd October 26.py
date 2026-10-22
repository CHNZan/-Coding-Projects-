#Q2
query = 'n'
number = float(input('Enter a number: '))
number_2 = float(input('Enter a 2nd number: '))
sub_total = number + number_2
query = input('Do you want to add another number? (y/n): ')
while query == 'y':
    number_3 = float(input('Enter another number: '))
    sub_total = sub_total + number_3
    query = input('Do you want to add another number? (y/n): ')
    
print('Total: ',sub_total)