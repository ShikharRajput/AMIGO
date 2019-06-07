import webbrowser
import os,sys
import random
from datetime import datetime
import snake,space,Zombie_shooter,car_race,game,weather,news
print(
      " .........................Hello am APEX..........................                          "
      )

hello_intent = ['hello', 'hi', 'hie', 'hey', 'yo','hlo','hii']
date_intent=("tell me date",'date please','show me date','date','show date')
time_intent=("tell me time",'time please','show me time','time','show time')
music_intent=("play music","play song","play any song","music","dj wale babu mera gana chala do","song","music")
game_intent=("play game","game")
weather_intent=("weather","today's weather","tell me weather","show me weather","weather please")
news_intent=("news","tell me news","show me news","news please","today's news")
calc_intent=("open calc","open calculater","calc","calculater")
while "TURE":
    #global usermessage
    usermessage = input("Enter your message : ")
    usermessage = usermessage.lower()
    
    #Membership Operators - in, not in
    if usermessage in hello_intent:
        print("Hi there...")
    
    elif usermessage in time_intent:
        curr_time=datetime.now().time()
        print("Current time is",curr_time)
    elif usermessage in date_intent:
        curr_date=datetime.now().date()
        print("Current date is",curr_date)
    elif usermessage in calc_intent:
        os.system('calc.exe')
    elif usermessage in music_intent:
        os.chdir("F:\\Music\\lata")
        s=input("Enter name of song or play any : ")
        s=s.lower()
        songs=os.listdir()
        while s=="any":
            song=random.choice(songs)
            os.startfile(song)
            print("-------playing--------",song)
            change=input("Happy with this or change : ")
            if change=="change" or change=="y" or change=="yes":
                s=="any"
            #elif change=="end" or change=="end task":
                #sys.exit()
            elif change=="n" or change=="no" or change=="exit":
                break
            else:
                break
        else:
            s=s+".mp3"
            
            for i in songs:
                i=i.lower()
                if s==i:
                    os.startfile(s)
                    break
            else:
                print("not found")

    elif usermessage in weather_intent:
        weather.main()
    elif usermessage in news_intent:
        news.main()
    elif usermessage in game_intent:
        game.main()        
    elif usermessage == "bye":
        print("..................Bye Thanks for Coming Dear....................")
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
            z=""
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
                    #print("oo")
                    break
                elif len(web)==1:
                    webbrowser.open(usermessage+'.com')
                    #print("ff")
                    break
            else:
                webbrowser.open(usermessage)
                #print("yy")
                
