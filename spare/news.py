def main():
    import requests,bs4

    api_address = 'https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=41a167fc850342dba19a7e12e4b555a2'

          
    json_data = requests.get(api_address).json()
    #data=bs4.BeautifulSoup(json_data,'lxml')
    #print(json_data)
    print("                .....TOP 10 HEADLINES.....                   ")
    for i in range(0,10):
        formatted_data = json_data['articles'][i]['title']
        print(i+1,":",formatted_data)
