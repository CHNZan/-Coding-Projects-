raining = input('Is it raining? ( yes / no ): ')
windy_question_activate = 'undefined'
if raining == 'no' or raining == 'No':
    print('Enjoy your day')
else:
    windy_question_activate = 'yes'

def windy_question():
    windy = input('Is it windy? ( yes / no ): ')
    if raining == 'yes' or raining == 'Yes':
        if windy == 'yes' or windy == 'Yes':
            print("It's too windy for an umbrella")
        elif windy == 'no' or windy == 'No':
            print('Take an umbrella')
        else:
            print('INVALID INPUT ( input has to be yes / no')
    else:
        print('INVALID INPUT ( input has to be yes / no')
        
if windy_question_activate == 'yes':
    windy_question()
else:
    pass

#NOTE: i had to use the define function so if the user replies 'no' to the raining question - the windy question doesn't get asked...