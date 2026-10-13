name = input('Enter your name: ')
phone_number = input('Enter your phone number: ') #no int() needed in case user inputs string (e.g: 089-347-9340)
age = int(input('Enter your age: '))
height = float(input('Enter your height: '))
eircode = input('Enter your eircode: ')

print(f'''
name: {name} , phone number: {phone_number}
name: {name} , eircode: {eircode}
age: {age} , height: {height}
name: {name} , phone number: {phone_number} , age: {age} , height: {height}
''')