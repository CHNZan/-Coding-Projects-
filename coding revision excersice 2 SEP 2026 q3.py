sentence = input('Enter a sentence: ')
a = 0
e = 0
i = 0
o = 0
u = 0
for letter in sentence:
    if letter == 'a':
        a = a + 1
    elif letter == 'e':
        e = e + 1
    elif letter == 'i':
        i = i + 1
    elif letter == 'o':
        o = o + 1
    elif letter == 'u':
        u = u + 1
    else:
        pass
    
print('Number of "a"(s)',a)
print('Number of "e"(s)',e)
print('Number of "i"(s)',i)
print('Number of "o"(s)',o)
print('Number of "u"(s)',u)