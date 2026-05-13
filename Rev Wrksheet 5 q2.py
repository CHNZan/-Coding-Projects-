string = input('Enter a string: ')
print('number of letters: ',len(string))

letter_int = 0

for letter in string:
    if letter == 'a' or letter == 'o' or letter == 'u'  or letter == 'i'  or letter == 'e' :
        letter_int = letter_int + 1
        
print('number of vowels: ',letter_int)