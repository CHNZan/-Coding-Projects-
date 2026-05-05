colour = input('Enter the colour of an item: ')
if colour == 'red' or colour == 'Red':
    fruit = input('Is it a fruit: ')
    if fruit == 'yes' or fruit == 'Yes':
        print('It could be an apple or tomato')
    elif fruit == 'no' or fruit == 'No':
        print('It could be a rose')
    else:
        print('Invalid input')
elif colour == 'yellow' or colour == 'Yellow':
    fruit = input('Is it a fruit: ')
    if fruit == 'yes' or fruit == 'Yes':
        print('It could be a banana')
    elif fruit == 'no' or fruit == 'No':
        print('It could be corn or marigold')
    else:
        print('Invalid input')
else:
    print('I cannot assist in identifying the item')