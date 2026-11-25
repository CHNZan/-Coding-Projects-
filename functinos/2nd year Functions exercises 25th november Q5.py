#Q5
def count_letters(word):
    counter = 0
    for loop in word:
        counter = counter + 1
    return counter

input_string = input('Enter a word: ')
print(count_letters(input_string))