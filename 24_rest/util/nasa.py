import urllib.request, json

api = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
def get_dict():
    with urllib.request.urlopen(api) as url:
        data = json.loads(url.read().decode())
        #print(data)
    return data
