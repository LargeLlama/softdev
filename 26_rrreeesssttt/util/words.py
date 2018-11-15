import json, urllib

API_LINK = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/"
API_KEY = "?key=4a0b1649-f508-4aae-a17b-03407ea06b6f"

def get_entry(word):
    response = urllib.urlopen(API_LINK + word + API_KEY)
    return json.loads(response.read())

def get_definition(word):
    entry = get_entry(word)

print(get_entry("lacrosse"))
