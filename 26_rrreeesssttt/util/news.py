import json, requests

API_KEY = "a842f08935ec4c4f8cbfa0ca729fc2c1"

def top_headlines(src):
    url = ('https://newsapi.org/v2/top-headlines?'
       'sources=' + src + '&'
       'apiKey=' + API_KEY)
    response = requests.get(url)
    return json.loads(response.text)

#dict = top_headlines('bbc-news')
#print(dict['articles'][0]['source'])
