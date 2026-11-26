#Q1
def num_test(num):
    if num > 10:
        return f'{num} > 10'
    elif num == 10:
        return f'{num} = 10'
    else:
        return f'{num} < 10'
    
num_input = float(input('Enter a number: '))
print(num_test(num_input))