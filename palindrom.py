def palindrom(string):
    letters = []
    for letter in range(len(string)-1,-1,-1):
        letters.append(string[letter])
    revers =''.join(letters)
    if revers == string:
        return True
    else:
        return False

print(palindrom('лепсспел'))

