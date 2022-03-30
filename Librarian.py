import json
from datetime import date

today = date.today()

newWord = input ('What new word have you read?\n')

with open('Library.json', 'r') as f: #Used open function to open json file
    personDict = json.load(f)

print(personDict) # Trying this example https://www.programiz.com/python-programming/json
