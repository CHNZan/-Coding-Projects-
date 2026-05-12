name = input('Please enter your name: ')
if name == 'Jerry' or name == 'jerry':
    print('Your meal is free , have a nice day Jerry!')
else:
    portions = int(input('Please enter the amount of portions: '))
    print('The total cost is €',portions * 5.90)