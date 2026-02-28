#exclusive ( 1 , 3 , 5 .... 95 , 97)
def exclusive():
    for x in range(1, 99):
        if x % 2 == 1:
            print(x)
            
#inclusive ( 1 , 3 , 5 ... 95 , 97 , 99)
def inclusive():
    for x in range(1, 100):
        if x % 2 == 1:
            print(x)

while True:
    input_ = input('Prompt: Do you wish to show all odd number between 1 and 99 inclusive or exclusive? ')
    
    if input_ == "inclusive":
        inclusive()
    elif input_ == "exclusive":
        exclusive()
    else:
        print("Invalid input. Please type 'inclusive' or 'exclusive'.")