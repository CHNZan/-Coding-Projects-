user_input=input('''Select from the following:
1.Celsius
2.Fahrenheit
''')
temp=float(input('Enter the temperature:'))
if user_input == str('1') or user_input == str('Celsius'):
    output = temp * ( 9 / 5 ) + 32
    temp_unit = str('℃')
    output_temp_unit = str('℉')
elif user_input == str('2') or user_input == str('Fahrenheit'):
    output = ( temp - 32 ) * ( 5 / 9 )
    temp_unit = str('℉')
    output_temp_unit = str('℃')
else:
    output = str('Error')

if output is str('Error'):
    print('Invalid temperature unit entred')
else:
    print(temp,temp_unit,' is ',output,output_temp_unit)