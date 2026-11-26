#Q3
def remove_letter(string,removed_letter):
    output = ''
    for loop in string:
        if loop == removed_letter:
            pass
        else:
            output = output + loop
    return output
            
removed_letter = input('Enter a letter you wish to remove from a string: ')
string = input('Enter string: ')
print(remove_letter(string,removed_letter))