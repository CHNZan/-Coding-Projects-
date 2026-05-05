age = int(input('Enter your age: '))
if age < 12:
    print('Fare = €2')
elif age > 65:
    travel_card = input('Do you have a travel card: ')
    if travel_card == 'yes' or travel_card == 'Yes':
        print('Fare = None')
    elif travel_card == 'no' or travel_card == 'No':
        print('Fare = €3')
    else:
        print('Invalid input')
elif age <= 0:
    print('Invalid age')
else:
    print('Fare = €5')