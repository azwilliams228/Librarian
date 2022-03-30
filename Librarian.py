from asyncio import set_event_loop
import json
from datetime import date

#with open('Library.json', 'a') as f:
    #newWord = input ('What new word have you read?\n')
    #today = date.today()
    #dict = '{ "Word" : "newWord", "Date" : "today" }'
    #person_dict = json.loads(dict)

#with open('Library.json', 'r') as f:
    #personalLibrary = json.load(f)

today = date.today()
word = "steven"
words = { "Word" : word, "Date" : today }
wordsjson = json.dumps(words, indent = 1, sort_keys = True, default = str) #Converts the string to a JSON string

#words_dict = json.loads(words)

print(wordsjson['Word'])
