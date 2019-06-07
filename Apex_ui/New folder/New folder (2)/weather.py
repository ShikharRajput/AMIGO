import bs4,requests
import urllib.request as url
api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=b87dfabf4c2b8dd5dbd7d2a2b5750117&q='
city = input("City Name : ")

weburl = api_address + city
web = url.urlopen(weburl)

data=bs4.BeautifulSoup(web,'lxml')
print(data)
result=data.find_all('div' , class_='widget-widget')


print(result)  #---->output with scrap info

for name in result:
    print(name.text)

