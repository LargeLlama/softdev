import json, urllib.request

API_LINK = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/"
API_KEY = "?key=4a0b1649-f508-4aae-a17b-03407ea06b6f"

def get_entry(word):
    try:
        response = urllib.request.urlopen(API_LINK + word + API_KEY)
        data = json.loads(response.read())
        return data[0]
    except:
        response = urllib.request.urlopen(API_LINK + 'lacrosse' + API_KEY)
        data = json.loads(response.read())
        return data[0]

   
def get_definition(word):
    entry = get_entry(word)
    if (type(entry) is str):
        entry = get_entry('lacrosse')
    return entry['shortdef'][0]

#debug
#print(get_definition('lacrosse'))
#print(get_definition(''))
#print(get_definition('' ))
#print(get_definition('test'))
#print(get_definition('baseball'))

