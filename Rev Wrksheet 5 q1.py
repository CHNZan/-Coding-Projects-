string = input('Enter a string: ')
print(len('Length: ',string))

for letter in string:
    if letter == 'a' or letter == 'o' or letter == 'u'  or letter == 'i'  or letter == 'e' :
        print(letter)
    else:
        pass