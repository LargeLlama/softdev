import json, urllib.request

API_LINK = 'https://api.darksky.net/forecast/'
API_KEY = '65661444800d8180135cd4c62317a82c'

def get_json(lat, lon):
    response = urllib.request.urlopen(API_LINK + API_KEY + '/' + str(lat) + ',' + str(lon))
    data = json.loads(response.read())
    return data

def get_temp(lat, lon):
    data = get_json(lat, lon)
    return data['currently']['temperature']

def get_summary(lat, lon):
    data = get_json(lat, lon)
    return data['minutely']['summary']

#print(get_temp(42.3601,-71.0589))
#print(get_summary(42.3601,-71.0589))
