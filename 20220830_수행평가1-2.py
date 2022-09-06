
def encrypt (word):
    for char in word:
        string = ''
        #print(char)
        if char == 'a' or char =='e'or char =='i'or char =='o'or char =='u':
            char='*'

        string += char
    return string

print(encrypt('ive'))


