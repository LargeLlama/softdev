import json, urllib.request

API_LINK = "https://api.icndb.com"

def get_joke():
    response = urllib.request.urlopen(API_LINK + '/jokes/random')
    data = json.loads(response.read())
    return data['value']['joke']

#print(get_joke())
