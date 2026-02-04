year = int(input('Enter the year:'))
month = int(input('Enter the month:'))
day = int(input('Enter the day: '))

error = bool('no')

if year > 0:
    pass
else:
    error = bool('yes')
   
if month >= 1 and month < 13:
    pass
else:
    error = bool('yes')
   
if day >= 1 and day < 32:
    pass
else:
    error = bool('yes')
   
if error == bool('yes'):
    print('invalid date')
else:
    pass