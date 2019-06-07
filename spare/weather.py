def main():
    import requests,bs4

    api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=b87dfabf4c2b8dd5dbd7d2a2b5750117&q='
    city = input("CITY NAME : ")


    '''import pyaudio
    import speech_recognition as sr

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Tell The Name of City")

        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
        except:
            print("Sorry")

    city = format(text)'''
    

    url = api_address + city

    json_data = requests.get(url).json()
    print(json_data)

    formatted_data = json_data['main']['temp']
    formatted_data_2 = json_data['weather'][0]['main']
    formatted_data_3 = json_data['main']['humidity']
    formatted_data_4 = json_data['main']['temp_min']
    formatted_data_5 = json_data['main']['temp_max']
    


    #formatted_data = (5/9)*(formatted_data - 32)
    formatted_data -= 273.15
    formatted_data_4 -= 273.15
    formatted_data_5 -= 273.15
    print(" TEMP : ","%.2f"%formatted_data,"C","\n",formatted_data_2,"\n","HUMIDITY : ",formatted_data_3,"%","\n","MIN_TEMP : ","%.2f"%formatted_data_4,"C","\n","MAX_TEMP : ","%.2f"%formatted_data_5,"C")
          
    for i in json_data:
        if i == "visibility":
            formatted_data_6 = json_data['visibility']
            print(" VISIBILITY : ",formatted_data_6,"m")

#,"\n","VISIBILITY : ",formatted_data_6,"m"
#print(json_data['sys']['sunrise'])
