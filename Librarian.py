
with open('Library.txt', 'w') as f:
    f.write('This is your dictionary.')
    newWord = input ('What new word have you read?\n')
    f.write(newWord)