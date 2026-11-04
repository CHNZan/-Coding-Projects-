#Q5
gender = input('Enter Gender: ')
if gender == 'male' or gender == 'Male':
    pronoun = 'Sir'
elif gender == 'female' or gender == 'Female':
    pronoun = 'Madam'
else:
    pronoun = ''
    
print('Good morning',pronoun)