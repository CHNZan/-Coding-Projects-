secret_number = 7
guess = int(input('Enter your guess: '))
if guess == secret_number:
    print('Correct answer!')
elif guess == secret_number + 1 or guess == secret_number - 1:
    print('Close enough. (±1) ')
else:
    print('Guess again! (not close enough)')