import json, requests

API_LINK = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/"
API_KEY = "?key=4a0b1649-f508-4aae-a17b-03407ea06b6f"

def get_entry(word):
    response = requests.get(API_LINK + word + API_KEY)
    data = json.loads(response.text)
    return data[0]

def get_definition(word):
    entry = get_entry(word)
    return entry['def'][0]['sseq'][0][0][1]['dt'][0][1][4:]

#print(get_definition('lacrosse'))
#print(get_definition('baseball'))

