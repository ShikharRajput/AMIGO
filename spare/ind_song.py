import webbrowser
import os,sys
import random
from datetime import datetime
import snake,space,Zombie_shooter
hello_intent = ['hello', 'hi', 'hie', 'hey', 'yo']
date_intent=("tell me date",'date please','show me date')
time_intent=("tell me time",'time please','show me time')
music_intent=("play music","play song","play any song","music","dj wale babu mera gana chala do")
game_intent=("play game","game")

while "TURE":

    usermessage = input("Enter your message : ")
    usermessage = usermessage.lower()

    #Membership Operators - in, not in
    if usermessage in hello_intent:
        print("Hi there...")
    elif usermessage.startswith('open'):
        web = usermessage.split()[1]
        webbrowser.open(web+'.com')
    elif usermessage in time_intent:
        curr_time=datetime.now().time()
        print("Current time is",curr_time)
    elif usermessage in date_intent:
        curr_date=datetime.now().date()
        print("Current date is",curr_date)
    elif usermessage in music_intent:
        os.chdir("F:\\Music\\lata")
        s=input("Enter name of song or play any : ")
        s=s.lower()
        songs=os.listdir()
        while s=="any":
            song=random.choice(songs)
            os.startfile(song)
            print("playing-",song)
            change=input("Happy with this or change or end task : ")
            if change=="change":
                s=="any"
            elif change=="end" or change=="end task":
                sys.exit()
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

    elif usermessage in game_intent:
        Game = input("SNAKE , SPACE ,Zombie Shooter : ")
        Game=Game.lower()
        if Game == "snake":
            snake.main()
        elif Game == "space":
            space.main()
        elif Game == "zombie" or Game == "zombie shooter" or Game == "zombieshooter":
            Zombie_shooter.main()
    elif usermessage == "bye":
        print("Bye")
        break
    else:
        print("I Don't Understand")
