
from tkinter import *
import pygame
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap,QIcon
from pygame.locals import *
import webbrowser
import urllib.request
import urllib.request as url
import os,random
from datetime import datetime
import snake,space,Zombie_shooter,car_race
import cv2

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 630, 561))
        self.label.setText("")
        self.label.setObjectName("label")
        self.image = QPixmap('back1.png')
        self.label.setPixmap(self.image)
        self.label.setObjectName("image")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(46, 35, 491, 41))
        self.label_2.setStyleSheet("font: 75 italic 28pt \"Algerian\";\n");

        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 150, 321, 61))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(394, 152, 61, 51))
        self.pushButton.setObjectName("pushButton")
        self.image = QIcon(QPixmap('mic.png'))
        self.pushButton.setIcon(self.image)
        self.pushButton.setObjectName("image")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 150, 61, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.image = QIcon(QPixmap('search2.png'))
        self.pushButton_2.setIcon(self.image)
        self.pushButton_2.setObjectName("image")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(42, 340, 511, 141))
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "        VIRTUAL ASSISTANT  "))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.clicked.connect(self.lineEdit2)



    def lineEdit2(self):

        date_intent = ['tell me date', 'date please', 'date', 'show me date']
        time_intent = ['tell me time', 'time please', 'time', 'show me time']
        hello_intent = ['hello', 'hi', 'hie', 'hey', 'yo', 'nameste']
        play_intent=['play song']
        game_intent = ("play game", "game")
        usermessage = self.lineEdit.text()
        usermessage = usermessage.lower()




        if usermessage in hello_intent:
            self.lineEdit_2.setText(random.choice(hello_intent))
        try:
          if usermessage  in play_intent:
              self.lineEdit_2.setText("playing songs.....")
              path = r'C:\Users\golat\PycharmProjects\zombi\streetfighter\sounds'
              os.chdir(path)
              songs = os.listdir()
              song = random.choice(songs)
              os.startfile(song)
        except BaseException as ex:
            print(ex)

        #for event in pygame.event.get():
            # print(event)
            #if event.type == pygame.QUIT:
               # pygame.quit()
                #quit()


        if usermessage.startswith('open'):
            self.lineEdit_2.setText("okay. Wait")
            web = usermessage.split()[1]
            webbrowser.open(web + '.com')
        try:
          if usermessage in time_intent:
            curr_time = str(datetime.now().time())
            self.lineEdit_2.setText(curr_time)

          if usermessage in date_intent:
            curr_date = str(datetime.now().date())
            self.lineEdit_2.setText(curr_date)

        except BaseException as ex:
          print(ex)

        try:
            if usermessage.startswith('meaning of '):
                # self.lineEdit_2.setText("okay. Wait")
                message = usermessage.split()[2]
                print(message)
                web = url.urlopen('https://en.oxforddictionaries.com/definition/' + message)

                data = bs4.BeautifulSoup(web, 'lxml')
                result = data.find_all('span', class_='ind')

                for name in result:
                    self.lineEdit_2.setText(name.text)
        except BaseException as ex:
            print(ex)

        try:
            if usermessage.startswith("add"):
                operand1 = int(usermessage.split()[1])
                operator = usermessage.split()[2]
                operand2 = int(usermessage.split()[3])
                Addition = operand1 + operand2
                self.lineEdit_2.setText(str(Addition))

            if usermessage.startswith("multiply"):
                operand1 = int(usermessage.split()[1])
                operator = usermessage.split()[2]
                operand2 = int(usermessage.split()[3])
                Addition = operand1 * operand2
                self.lineEdit_2.setText(str(Addition))

            if usermessage.startswith("divide"):
                operand1 = int(usermessage.split()[1])
                operator = usermessage.split()[2]
                operand2 = int(usermessage.split()[3])
                Addition = operand1 / operand2
                self.lineEdit_2.setText(str(Addition))

            if usermessage.startswith("subtract"):
                operand1 = int(usermessage.split()[1])
                operator = usermessage.split()[2]
                operand2 = int(usermessage.split()[3])
                Addition = operand1 - operand2
                self.lineEdit_2.setText(str(Addition))

        except BaseException as ex:
            print(ex)
        try:
          if usermessage in game_intent:
            pygame.init()

            width = 900
            height = 500
            red = 0, 0, 255
            black = 0, 0, 0
            screen = pygame.display.set_mode((width, height))

            Snake = pygame.image.load("snakeimg.jpg")
            Space = pygame.image.load("space.png")
            Zombie = pygame.image.load("zombie.jpg")
            Carrace = pygame.image.load("car.jpg")

            screen.blit(Snake, (20, 180,))
            screen.blit(Space, (240, 180,))
            screen.blit(Zombie, (460, 180,))
            screen.blit(Carrace, (680, 180,))

            while True:
                rect_1 = pygame.Rect(20, 180, 200, 150)
                rect_2 = pygame.Rect(240, 180, 200, 150)
                rect_3 = pygame.Rect(460, 180, 200, 150)
                rect_4 = pygame.Rect(680, 180, 200, 150)

                pos_x, pos_y = pygame.mouse.get_pos()
                rect_5 = pygame.Rect(pos_x, pos_y, 10, 10)

                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if rect_5.colliderect(rect_1):
                            snake.main()
                        elif rect_5.colliderect(rect_2):
                            space.main()
                        elif rect_5.colliderect(rect_3):
                            Zombie_shooter.main()
                        elif rect_5.colliderect(rect_4):
                            car_race.main()
        except BaseException as ex:
            print(ex)

        try:
          if usermessage.startswith("weather"):
            city= usermessage.split()[2]
            api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=b87dfabf4c2b8dd5dbd7d2a2b5750117&q='
            url = api_address + city
            json_data = requests.get(url).json()
            # print(json_data)
            formatted_data = json_data['main']['temp']
            formatted_data_2 = json_data['weather'][0]['main']
            formatted_data_3 = json_data['main']['humidity']
            formatted_data_4 = json_data['main']['temp_min']
            formatted_data_5 = json_data['main']['temp_max']

            # formatted_data = (5/9)*(formatted_data - 32)
            formatted_data -= 273.15
            formatted_data_4 -= 273.15
            formatted_data_5 -= 273.15


            #self.lineEdit_2.text()


            print(" TEMP : ", "%.2f" % formatted_data, "C", "\n", formatted_data_2, "\n", "HUMIDITY : ",
                  formatted_data_3, "%", "\n", "MIN_TEMP : ", "%.2f" % formatted_data_4, "C", "\n", "MAX_TEMP : ",
                  "%.2f" % formatted_data_5, "C")


            for i in json_data:
                if i == "visibility":
                    formatted_data_6 = json_data['visibility']
                    print(" VISIBILITY : ", formatted_data_6, "m")

            dataset = {"temp": formatted_data,
                                "humidity": formatted_data_3,
                                "mintemp": formatted_data_4,
                                "maxtemp": formatted_data_5,
                                "visibility": formatted_data_6}
            self.lineEdit_2.setText(str(dataset))
        except BaseException as ex:
            print(ex)

        if usermessage.startswith("news"):


            api_address = 'https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=41a167fc850342dba19a7e12e4b555a2'

            json_data = requests.get(api_address).json()
            # data=bs4.BeautifulSoup(json_data,'lxml')
            # print(json_data)
            print("                .....TOP 10 HEADLINES.....                   ")
            for i in range(0, 10):
                formatted_data = json_data['articles'][i]['title']
                print(i + 1, ":", formatted_data)

        if usermessage.startswith("on"):


            cap = cv2.VideoCapture(0)  # 0 gives default camera
            while True:
                ret, img = cap.read()
                cv2.imshow('result', img)
                # print(cv2.waitKey(1))
                if cv2.waitKey(1) == 27:  # 27 is ASCII code for Esc
                    break
            cap.release()
            cv2.destroyAllWindows()

        try:
         if usermessage.startswith("face"):
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
                    for x, y, w, h in faces:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 4)
                    for x, y, w, h in eyes:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)
                    # for x,y,w,h in smile:
                    # cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255),4)
                    cv2.imshow('result', img)
                    if cv2.waitKey(1) == 27:
                        break
                else:
                    print("Camera not working")
            cap.release()
            cv2.destroyAllWindows()
        except BaseException as ex:
            print(ex)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

