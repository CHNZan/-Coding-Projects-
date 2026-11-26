#Q2
def digit_count(number):
    counter = 0
    for digit in number:
        counter = counter + 1
    return counter
        
num_input = input('Enter a number: ')
print(digit_count(num_input))