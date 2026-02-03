price = float(input('Enter the price of your product: '))
region = input('''Select your region:
1.National
2.Foreign
Enter here:''')

if region == str('1') or region == str('National'):
    total = price * (1 + 0.08)
elif region == str('2') or region == str('Foreign'):
    total = price * (1 + 0.18)
else:
    print('invalid region')
    total = str('Error')

if total is not str('Error'):
    print('Total cost: ',total)
else:
    pass