from tkinter import *
import pygame
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap,QIcon
from pygame.locals import *
import os,random
import snake,space,Zombie_shooter,car_race
class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 420)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Label_0 = QtWidgets.QLabel(self.centralwidget)
        self.Label_0.setGeometry(QtCore.QRect(-20, -10, 630, 420))
        self.Label_0.setObjectName("Label_0")

        self.image = QPixmap('bk.jpg')
        self.Label_0.setPixmap(self.image)
        self.Label_0.setObjectName("image")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 20, 400, 100))
        self.label.setStyleSheet("font: italic 200pt \"Algerian\";")
        self.label.setObjectName("label")
        self.label.setStyleSheet('color:white;')

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 110, 261, 41))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 190, 520,120 ))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.PusButton = QtWidgets.QPushButton(self.centralwidget)
        self.PusButton.setGeometry(QtCore.QRect(400, 110, 27, 41))
        self.PusButton.setText("")
        self.PusButton.setObjectName("label_2")
        self.image = QIcon(QPixmap('mic.png'))
        self.PusButton.setIcon(self.image)
        self.PusButton.setIconSize(QtCore.QSize(25,41))
        self.PusButton.setObjectName("image")




        self.PusButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.PusButton2.setGeometry(QtCore.QRect(521, 110, 25, 41))
        self.PusButton2.setText("")
        self.PusButton2.setObjectName("label_3")
        self.image = QIcon(QPixmap('search2.png'))
        self.PusButton2.setIcon(self.image)
        self.PusButton2.setIconSize(QtCore.QSize(25,41))
        self.PusButton2.setObjectName("image")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 411, 21))
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
        self.label.setText(_translate("MainWindow", "VIRTUAL ASSISTANT"))

        self.PusButton2.clicked.connect(self.lineEdit2)




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
        except BaseException as ex:
          print(ex)
          if usermessage in date_intent:
            curr_date = str(datetime.now().date())
            self.lineEdit_2.setText(curr_date)

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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())

