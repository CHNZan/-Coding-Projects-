AB = float(input('Enter AB: '))
BC = float(input('Enter BC: '))
CD = float(input('Enter CD: '))
DA = float(input('Enter DA: '))
I = float(input('Enter I: '))

if  AB == BC:
    if AB == CD:
        if BC == DA:
            if I == 90:
                print("It's a square")
            else:
                print("It's a rhombus")
        else:
            print("It's an irregular quadilateral")
    else:
        print("It's an irregular quadilateral")
else:
    if AB == CD:
        if BC == DA:
            if I == 90:
                print("It's a rectangle")
            else:
                print("It's a parralellogram")
        else:
            print("It's an irregular quadilateral")
    else:
        print("It's an irregular quadilateral")