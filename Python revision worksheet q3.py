age = int(input('Enter your age: '))
if age >= 18:
    _license = input('Do you have a license: ')
    if _license == 'yes' or _license == 'Yes':
        print('You can rent a car (eligible)')
    elif _license == 'no' or _license == 'No':
        print('You are cannot rent a car(not eligible)')
    else:
        print('Invalid input')
elif age <= 0:
    print('Invalid age')
else:
    print('You are cannot rent a car(not eligible)')