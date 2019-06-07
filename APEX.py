import webbrowser
import bs4
import os,sys
import requests,bs4
import random
import cv2
import pyaudio
import speech_recognition as sr
import pyttsx3
import time #from datetime import datetime
import urllib.request as url
import pygame
from pygame.locals import *
import snake,space,Zombie_shooter,car_race,project,StreetFighter

print(
      " .........................Hello am Amigo..........................                          "
      )

hello_intent = ['hello', 'hi', 'hie', 'hey', 'yo','hlo','hii','hello hello']
date_intent=("tell me date",'date please','show me date','date','show date',"what's the date")
time_intent=("tell me time",'time please','show me time','time','show time',"what's the time")
jokes_intent = ['joke','joke of the day','joke please','tell me a joke','say something funny','tell me something funny','make me laugh']
tnd_intent = ['play truth and dare','truth and dare','random fun','truth or dare']
diction_intent = ['search in dictionary','dictionary please','dict','dictionary']
quotes_intent =['quote of the day','some quotes please','quote']

music_intent=("play music","play song","play any song","music","dj wale babu mera gana chala do","song","music",'play me a song')
game_intent=("play game","game","do you have game",'i am getting bore','i want to play game','i want to play some games','games')
weather_intent=("weather","today's weather","tell me weather","show me weather","weather please")
news_intent=("news","tell me news","show me news","news please","today's news",'news headlines')
calc_intent=("open calc","open calculator","calc","calculator")
camera_intent=("open camera","camera")
call_intent=("where is my phone","call me",'call','i forget my phone someware','help me to find my phone')
face_intent=("face detection","detect my face","open face detection")

reply_hello_intent= ['hiya!! How can I help?','Namasteyy!! How can I help? ','Hello!! How can I help?','Welcome back... What can I do for you','Hey... How can I help']
reply_jokes_intent = ['What did the traffic light say to the car???? \n Don’t look! I’m about to change.','Where do you find a cow with no legs????? \n Right where you left it.','What did the left eye say to the right eye??? \n Between you and me, something smells.','What do you call bears with no ears??? \n B–','They all laughed when I said I wanted to be a comedian... \n Well, they’re not laughing now!','it\'s hard to explain puns to kleptomaniacs they always take things literally.....','what did one introvert say to the other introvert???? \n Absolutely nothing and they quickly parted ways']
truth_intent = ['What was the last thing you searched for on your phone?','Of the people in this room, who do you want to trade lives with?','Have you ever practiced kissing in a mirror?','What is your guilty pleasure?','Who is the sexiest person in this room?','Have you ever ding dong ditched someone?','Have you ever been stood up on a date?','If you could be reincarnated into anyone\'s body, who would you want to become?']
dare_intent = ['Sing and dance in the street like crazy.','Yell out the first word that comes to your mind right now','Make up a story about the item to your right.','Sing everything you say for the next 10 minutes.','Say the alphabet backward in 15 seconds.','Sing a song all the way through to the end.','Go a whole minute without blinking.','Say “banana” after everything you say until it is your turn again.','Say “banana” after everything you say until it is your turn again.','Give a massage to a companion for 5 minutes.']
bye_intent = ['bye','bye bye','ok bye','see you later','exit','shut down']

reply_intent = ['Ok','Ok here you go','done anything else','whatever you say']

def reply(x):
    engine = pyttsx3.init()
    engine.say(x)
    engine.setProperty('rate',120)  #120 words per minute
    engine.setProperty('volume',0.9) 
    engine.runAndWait()

def voicer():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Wish me Anything")

        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            #print("You said : {}".format(text))
            text = format(text)
            text = text.lower()
            if text is not None:
                return(text)
        except:
            print("                             Sorry did not hear you")

def voicer2():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        #print("Wish Anything")

        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            #print("You said : {}".format(text))
            text = format(text)
            text = text.lower()
            return(text)
        except:
            print("                             Sorry did not hear you")
            reply("Sorry did not hear you")
            

def twi():
    import os
    from twilio.rest import client
    # import twilio
    # import Client

    account_sid = "AC26fe88618e0be12f63a17ed7c411bcc8"
    auth_token = "52e414309956ce85112969bc34ebbf0a"

    C = client.TwilioRestClient(account_sid,auth_token)
    #c = cli(account_sid,auth_token)

    call = C.calls.create(
        to = "+917503169933",
        from_="+13612453684",
        url="http://demo.twilio.com/docs/voice.xml"
        )

def game():
    pygame.init()

    width = 900
    height = 500
    red = 0,0,255
    black = 0,0,0
    screen = pygame.display.set_mode((width,height))

    Snake = pygame.image.load("snakeimg.jpg")
    Space = pygame.image.load("space.png")
    Zombie = pygame.image.load("zombie.jpg")
    Carrace = pygame.image.load("car.jpg")
    PlantNZombie = pygame.image.load("plantNzombie.jpg")
    StreetFight = pygame.image.load("sf.jpg")
    
    screen.blit(Snake,(20,280,))
    screen.blit(Space,(240,280,))
    screen.blit(Zombie,(460,280,))
    screen.blit(Carrace,(680,280,))
    screen.blit(PlantNZombie,(460,70,))
    screen.blit(StreetFight,(240,70,))
    
    while True:
        rect_1 = pygame.Rect(20,280,200,150)
        rect_2 = pygame.Rect(240,280,200,150)
        rect_3 = pygame.Rect(460,280,200,150)
        rect_4 = pygame.Rect(680,280,200,150)
        rect_5 = pygame.Rect(460,70,200,150)
        rect_6 = pygame.Rect(240,70,200,150)
        
        pos_x,pos_y = pygame.mouse.get_pos()
        rect = pygame.Rect(pos_x,pos_y,10,10)

        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if rect.colliderect(rect_1):
                    snake.main()
                elif rect.colliderect(rect_2):
                    space.main()
                elif rect.colliderect(rect_3):
                    Zombie_shooter.main()
                elif rect.colliderect(rect_4):
                    car_race.main()
                elif rect.colliderect(rect_5):
                    project.main()
                elif rect.colliderect(rect_6):
                    StreetFighter.main()


    
def quote():
    api_address = 'http://quotes.rest/qod.json?category=inspire'
    json_data = requests.get(api_address).json()
    #print(json_data)
    json_data = json_data["contents"]["quotes"][0]["quote"]
    print(json_data)
    #reply(json_data)
    return(json_data)
    
def news():
    
    api_address = 'https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=41a167fc850342dba19a7e12e4b555a2'

          
    json_data = requests.get(api_address).json()
    #data=bs4.BeautifulSoup(json_data,'lxml')
    #print(json_data)
    print("                .....TOP 10 HEADLINES.....                   ")
    for i in range(0,10):
        formatted_data = json_data['articles'][i]['title']
        print(i+1,":",formatted_data)

    reply("                                 Here I am leaving you with recent Top 10 news followed by 1st headline")
    reply(json_data['articles'][0]['title'])


def weather():

    api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=b87dfabf4c2b8dd5dbd7d2a2b5750117&q='
    print("                                 Which CITY : ")
    reply("which city")
    city = voicer2()

    while city is None:
        city = voicer2()
    r="Okay here's the temperature of"+city
    reply(r)

    url = api_address + city

    json_data = requests.get(url).json()
    #print(json_data)

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

    formatted_data="%.2f"%formatted_data+"degree celcius"
    reply(formatted_data)

#,"\n","VISIBILITY : ",formatted_data_6,"m"
#print(json_data['sys']['sunrise'])

def faceD():
    
    dataset = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
    smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")
    cap = cv2.VideoCapture(0)

    while True:
        ret, img = cap.read()
        if ret:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = dataset.detectMultiScale(gray)
            eyes = eye_cascade.detectMultiScale(gray)
            smile = smile_cascade.detectMultiScale(gray)
            for x,y,w,h in faces:
                cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0),4)
            for x,y,w,h in eyes:
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),4)
            #for x,y,w,h in smile:
                #cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255),4)
            cv2.imshow('result', img)
            if cv2.waitKey(1) == 27:
                break
        else:
            print("Camera not working")
    cap.release()
    cv2.destroyAllWindows()

def camera():

    cap = cv2.VideoCapture(0) #0 gives default camera
    while True:
        ret, img = cap.read()
        cv2.imshow('result', img)
        #print(cv2.waitKey(1))
        if cv2.waitKey(1) == 27: # 27 is ASCII code for Esc
            break
    cap.release()
    cv2.destroyAllWindows()
    
chance = 3
reply("Hello am Amigo, Your virtual friend. You may wish me anything, I will try to help you")
while "TRUE":
    #global usermessage
    #usermessage = input("Enter your message : ")
    usermessage = voicer()
    #TextToVoice.main(usermessage)
    #usermessage = usermessage.lower()
    
    #Membership Operators - in, not in
    if usermessage is not None:
        chance = 3
        
    if usermessage is None:
        chance -= 1
        if chance == 0:
            print("                         You are not responding, So I am switching off.... bye my friend")
            reply("Sorry did not hear you, you are not responding, So I am switching off....\n bye my friend")
            break
        print("                                 Please say it again.....")
        reply("Sorry did not hear you, Please say it again.....")
        
    elif usermessage in hello_intent:
        r = random.choice(reply_hello_intent)
        print("                            ",r)
        reply(r)
    
    elif usermessage in time_intent:
        curr_time = time.ctime()                #curr_time=datetime.now().time()
        #print("Current time is",curr_time)
        #curr_time=str(curr_time)

        curr_time=str(curr_time)
        #print(curr_time)
        a=curr_time[11:13]+" Hour "+curr_time[14:16]+" Minutes "+curr_time[17:19]+" Seconds"
        print("                            ",a)
        
        reply(a)
        
    elif usermessage in date_intent:
        curr_date = time.ctime()          #curr_date=datetime.now().date()
        a=curr_date[:4] + curr_date[4:11] + curr_date[20:]
        print("                            ",a)
        
        reply(a)    

    elif usermessage in jokes_intent :
        #while usermessage in jokes_intent:
        print("OK, here you go:")
        j_reply = random.choice(reply_jokes_intent)
        print(j_reply)
        joke_reply = "OK, here you go:" + j_reply
        reply(joke_reply)
        #input_2 = input("One more : ")
        #input_2 = input_2.lower()
            #if input_2 == 'one more' or input_2=="y":
                #usermessage=="joke"
            #else:
                #break
    elif usermessage in diction_intent:
        d = "                               Tell me the word you want to find meaning of"
        print(d)
        reply(d)
        user_input = voicer2()
        while user_input is None:
            user_input = voicer2()
        web = url.urlopen('https://en.oxforddictionaries.com/definition/'+user_input)
        data = bs4.BeautifulSoup(web, 'lxml')
        result = data.find_all('span', class_='ind')
        for name in result:
            print("\n",name.text)
            a=name.text
            u = "meaning of "+ user_input
            reply(u)
            reply(a)
            '''c=0
            for i in a:
                if i == ".":
                    b=a[:a.index(i)+1]
                    #print(b)
                    reply(b)
                    c=1
                    break
                elif c == 1:
                    break
            #reply(b)'''

            
    elif usermessage in tnd_intent:
        input_3 = input("\n\n Choose TRuth OR DAre :\t")
        input_3 = input_3.lower()
        if input_3 == 'truth':
            t_reply = random.choice(truth_intent)
            print(t_reply)
        else:
            d_reply = random.choice(dare_intent)
            print(d_reply)
    elif usermessage in calc_intent:
        reply(random.choice(reply_intent))
        os.system('calc.exe')
    elif usermessage in music_intent:
        os.chdir("F:\\Music\\lata")
        songs=os.listdir()
        song=random.choice(songs)
        os.startfile(song)
        print("                             -------playing--------",song)
        reply(song)

    elif usermessage in weather_intent:
        weather()
    elif usermessage in news_intent:
        news()
    elif usermessage in game_intent:
        reply("I have some games for you")
        game()
    elif usermessage in camera_intent:
        reply(random.choice(reply_intent))
        camera()
    elif usermessage in face_intent:
        reply(random.choice(reply_intent))
        faceD()
    elif usermessage in call_intent:
        #twi()
        reply("                             Your phone should be ringing after some seconds")
        twi()
    elif usermessage in quotes_intent:
        q_reply = quote()
        reply("here's the quote of the day")
        reply(q_reply)
    elif usermessage in bye_intent:
        print("..................Bye Thanks for Coming Dear....................")
        print(" Here I leave you with the quote of the day.....")

        reply("Bye Thanks for Coming Dear  Here I leave you with the quote of the day.....")
        b_quote = quote()
        reply(b_quote)
        '''q_reply = random.choice(quotes_intent)
        print(q_reply)
        parting_word = "Bye Thanks for Coming Dear  Here I leave you with the quote of the day....." +  q_reply
        reply(parting_word)'''
        break
    else:
        
        a=''
        b=''
        for i in usermessage:
            #print(i)
            if i == "+":
                c=usermessage.index(i)
                a+=usermessage[0:c]
                b+=usermessage[c+1:]
                #print(a,b)
                print(int(a)+int(b))
                break
            elif i == "-":
                c=usermessage.index(i)
                a+=usermessage[0:c]
                b+=usermessage[c+1:]
                #print(a,b)
                print(int(a)-int(b))
                break
            elif i == "*":
                c=usermessage.index(i)
                a+=usermessage[0:c]
                b+=usermessage[c+1:]
                #print(a,b)
                print(int(a)*int(b))
                break
            elif i == "/":
                c=usermessage.index(i)
                a+=usermessage[0:c]
                b+=usermessage[c+1:]
                #print(a,b)
                print(int(a)/int(b))
                break
        else:
            a=1
            z=""
            w=["facebook","gmail","youtube"]
            if usermessage in w:
                webbrowser.open(usermessage+'.com')
                u = "Opening " + usermessage
                print("                            ",u)
                reply(u)
                a=0
            web=usermessage.split()
            for i in web:
                
                if i=="open":
                    a=web.index(i)
                    #print(a)
                    for j in range(a+1,len(web)):
                        if j == len(web)-1:
                            z+= web[j]
                        else:
                            z+=web[j]+" "
                    webbrowser.open(z+'.com')
                    u = "Opening " + z
                    print("                            ",u)
                    reply(u)
                    #print("oo")
                    a=0
                    break
               
                
            if a==1:
                #diver = webdriver.Googlechrome()
                #driver.get("https://www."+usermessage)
                webbrowser.open(usermessage)
                u = "Searching in web " + usermessage
                reply(u)
                #print("yy")
                    
