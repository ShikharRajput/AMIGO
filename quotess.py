import requests,bs4
'''response = unirest.post("https://andruxnet-random-famous-quotes.p.rapidapi.com/?count=10&cat=movies",
  headers={
    "X-RapidAPI-Host": "andruxnet-random-famous-quotes.p.rapidapi.com",
    "X-RapidAPI-Key": "7d44d1b4dcmsh89e99c245c83847p17a669jsn02bd85965f4f",
    "Content-Type": "application/x-www-form-urlencoded"
  }
)'''

api_address = 'http://quotes.rest/qod.json?category=inspire'
json_data = requests.get(api_address).json()
#print(json_data)
print(json_data["contents"]["quotes"][0]["quote"])
