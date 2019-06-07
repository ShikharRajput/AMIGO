from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import webbrowser
import os
import random
import glob
from datetime import datetime
import bs4
import urllib.request
import urllib.request as url
import random
import requests
import snake,space,Zombie_shooter,car_race



class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1237, 744)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 10, 571, 101))
        self.label.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 170, 641, 121))
        self.lineEdit.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(950, 230, 251, 61))
        self.pushButton.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")


        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(720, 200, 131, 81))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.image = QPixmap('Untitled.png')
        self.label_2.setPixmap(self.image)
        self.label_2.setObjectName("image")


        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 410, 641, 91))
        self.lineEdit_2.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1237, 31))
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
        self.label.setText(_translate("MainWindow", "Personal ChatBot"))
        self.lineEdit.setText(_translate("MainWindow", "Enter your message..."))
        self.pushButton.setText(_translate("MainWindow", "SEARCH"))
        self.lineEdit_2.setText(_translate("MainWindow", "What Can I Do For You ?"))
        self.pushButton.clicked.connect(self.lineEdit2)

        #usermessage = self.lineEdit.text()
        #usermessage = usermessage.lower()
    def lineEdit2(self):

          date_intent = ['tell me date', 'date please', 'date', 'show me date']
          time_intent = ['tell me time', 'time please', 'time', 'show me time']
          hello_intent = ['hello', 'hi', 'hie', 'hey', 'yo', 'nameste']
          dictionary_intent = ['meaning of' ]
          game_intent = ("play game", "game")
          play_intent=['play song']
          usermessage = self.lineEdit.text()
          usermessage = usermessage.lower()





          if usermessage in hello_intent:
            self.lineEdit_2.setText("hellooo there jyoti ")
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

          try:
             if usermessage.startswith('open'):
               self.lineEdit_2.setText("okay. Wait")
               web = usermessage.split()[1]
               webbrowser.open(web + '.com')

          except BaseException as ex:
                 print(ex)

          try:
               if usermessage in time_intent:
                  curr_time = str(datetime.now().time())
                  self.lineEdit_2.setText(curr_time)

          except BaseException as ex:
                  print(ex)

          try:
             if usermessage in date_intent:
                curr_date = str(datetime.now().date())
                self.lineEdit_2.setText(curr_date)

          except BaseException as ex:
              print(ex)
          try:
              if usermessage.startswith('meaning of '):
                  #self.lineEdit_2.setText("okay. Wait")
                  message= usermessage.split()[2]
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
                operator=usermessage.split()[2]
                operand2 = int(usermessage.split()[3])
                Addition = operand1 + operand2
                self.lineEdit_2.setText(str(Addition))

              if usermessage.startswith("multiply"):
                operand1 = int(usermessage.split()[1])
                operator=usermessage.split()[2]
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
                operator=usermessage.split()[2]
                operand2 = int(usermessage.split()[3])
                Addition = operand1 - operand2
                self.lineEdit_2.setText(str(Addition))

              if  usermessage in game_intent:
                self.lineEdit_2.setText("snake")
                if self.pushButton.clicked.connect(self.lineEdit_2):

                  Game = self.lineEdit.text()
                Game = Game.lower()

                if Game == "snake":
                  snake.main()
                elif Game == "space":
                  space.main()
                elif Game == "zombie" or Game == "zombie shooter" or Game == "zombieshooter":
                  Zombie_shooter.main()
                elif Game == "car race" or Game == "car" or Game == "race" or Game == "carrace":
                    car_race.main()
          except BaseException as ex:
               print(ex)


if  __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())