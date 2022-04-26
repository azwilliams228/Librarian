import json
from datetime import date

#Notes:
#dictName[key] = value this appends
#print(write_file.read()) #you can only read it once when you open it.
#dumps dumps to a json string from a dictionary
#File is closed automatically as 'with' block is exited.
tempLibrary = ''

#1. Open existing json file as a readable object named read_file.
with open('Library.json', mode = 'r', encoding = 'utf8') as read_file:

    #2. Convert the json file into a dictionary
    libraryDictionary = json.loads(read_file.read())
    
    #3. Add items to the dictionary.
    libraryDictionary['Word_2'] = {}
    libraryDictionary['Word_2']['Word'] = 'Amphetamine'
    libraryDictionary['Word_2']['Book'] = 'Blitzed'
    libraryDictionary['Word_2']['Date'] = str(date.today())

    #4. Convert the dictionary back into a json string.
    libraryJsonString = json.dumps(libraryDictionary)

#Check what the dictionary looks like
print(libraryJsonString)

#5. Open existing json file as a writeable object named write_file.
with open('Library.json', mode = 'w', encoding= 'utf8') as write_file:

    #6. Overwrite existing data with new json string.
    write_file.write(libraryJsonString)
