from distutils.file_util import write_file # im not sure if this line is actually necessary 
import json
from datetime import date

today = date.today()

def libe():
    newWord = input ('What new word have you read?\n')
    with open('Library.json', 'w') as write_file: #Open json file, with write privelige
        json.dump(newWord, write_file, separators = ", ")
        myLibe = json.load(f)
        #dict = '{ "Word" : "newWord", "Date" : "today" }'
    
libe()

print(myLibe)
