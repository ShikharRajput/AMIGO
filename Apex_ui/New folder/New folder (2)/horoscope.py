import requests,bs4

api_address = 'https://cricapi.com/api/cricketScore?apikey=le2jnRmPadWSKb9YpLLd7pcCaMy1&unique_id=1034809'
          
json_data = requests.get(api_address).json()
#data=bs4.BeautifulSoup(json_data,'lxml')
print(json_data)
#print("                .....TOP 10 HEADLINES.....                   ")

print("NEXT MATCH")
api_address = 'https://cricapi.com/api/cricketScore?apikey=le2jnRmPadWSKb9YpLLd7pcCaMy1'
          
json_data = requests.get(api_address).json()
print(json_data)
