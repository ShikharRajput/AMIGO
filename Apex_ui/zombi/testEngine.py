from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from PyQt5.QtWidgets import QMessageBox

connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             port = 3306,
                             db = 'databasetechEngine',
                             autocommit = True)

cursor = connection.cursor()

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1283, 808)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 30, 451, 61))
        self.label.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 400, 311, 71))
        self.pushButton.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(890, 400, 311, 71))
        self.pushButton_2.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(60, 280, 311, 61))
        self.comboBox.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(890, 280, 311, 61))
        self.comboBox_2.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1291, 771))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(440, 20, 431, 61))
        self.label_2.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(70, 180, 411, 61))
        self.label_3.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(70, 280, 411, 61))
        self.label_4.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(70, 380, 411, 61))
        self.label_5.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(70, 480, 411, 61))
        self.label_6.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(660, 170, 381, 71))
        self.lineEdit.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(660, 270, 381, 71))
        self.lineEdit_2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(660, 380, 381, 71))
        self.lineEdit_3.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_3.setGeometry(QtCore.QRect(660, 490, 381, 51))
        self.comboBox_3.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(470, 610, 341, 81))
        self.pushButton_3.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1291, 751))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(490, 30, 471, 71))
        self.label_7.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(120, 220, 411, 71))
        self.label_8.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(120, 370, 411, 71))
        self.label_9.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(630, 210, 431, 81))
        self.lineEdit_4.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(630, 360, 431, 81))
        self.lineEdit_5.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(490, 570, 271, 71))
        self.pushButton_4.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 1291, 761))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.comboBox_4 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_4.setGeometry(QtCore.QRect(600, 110, 381, 71))
        self.comboBox_4.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(110, 110, 421, 71))
        self.label_10.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_5.setGeometry(QtCore.QRect(420, 340, 331, 71))
        self.pushButton_5.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 1291, 771))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_6.setGeometry(QtCore.QRect(20, 50, 1181, 81))
        self.lineEdit_6.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_7.setGeometry(QtCore.QRect(20, 200, 471, 61))
        self.lineEdit_7.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_8.setGeometry(QtCore.QRect(720, 200, 471, 61))
        self.lineEdit_8.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_9.setGeometry(QtCore.QRect(20, 360, 471, 61))
        self.lineEdit_9.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_10.setGeometry(QtCore.QRect(720, 360, 471, 61))
        self.lineEdit_10.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_11.setGeometry(QtCore.QRect(400, 510, 471, 61))
        self.lineEdit_11.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_6.setGeometry(QtCore.QRect(470, 650, 291, 61))
        self.pushButton_6.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_7.setGeometry(QtCore.QRect(940, 650, 291, 61))
        self.pushButton_7.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setGeometry(QtCore.QRect(0, 0, 1301, 761))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_11 = QtWidgets.QLabel(self.frame_5)
        self.label_11.setGeometry(QtCore.QRect(30, 40, 1201, 71))
        self.label_11.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_11.setObjectName("label_11")
        self.radioButton = QtWidgets.QRadioButton(self.frame_5)
        self.radioButton.setGeometry(QtCore.QRect(40, 220, 281, 71))
        self.radioButton.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_5)
        self.radioButton_2.setGeometry(QtCore.QRect(40, 310, 281, 71))
        self.radioButton_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame_5)
        self.radioButton_3.setGeometry(QtCore.QRect(40, 400, 281, 71))
        self.radioButton_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame_5)
        self.radioButton_4.setGeometry(QtCore.QRect(40, 500, 281, 71))
        self.radioButton_4.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.radioButton_4.setObjectName("radioButton_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_8.setGeometry(QtCore.QRect(710, 630, 361, 81))
        self.pushButton_8.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.pushButton_8.setObjectName("pushButton_8")
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setGeometry(QtCore.QRect(0, 0, 1321, 751))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_12 = QtWidgets.QLabel(self.frame_6)
        self.label_12.setGeometry(QtCore.QRect(130, 140, 331, 71))
        self.label_12.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_6)
        self.label_13.setGeometry(QtCore.QRect(140, 280, 331, 71))
        self.label_13.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame_6)
        self.label_14.setGeometry(QtCore.QRect(670, 140, 331, 71))
        self.label_14.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_6)
        self.label_15.setGeometry(QtCore.QRect(670, 280, 331, 71))
        self.label_15.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_15.setObjectName("label_15")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1283, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.frame.hide()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Welcome to Test Engine"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.pushButton_2.setText(_translate("MainWindow", "Register"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Teacher"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Student"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Teacher"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Student"))
        self.label_2.setText(_translate("MainWindow", "Regsitration Form"))
        self.label_3.setText(_translate("MainWindow", "Enter ID"))
        self.label_4.setText(_translate("MainWindow", "Enter Name"))
        self.label_5.setText(_translate("MainWindow", "Enter Password"))
        self.label_6.setText(_translate("MainWindow", "Choose Branch"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "CS/IT"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "EE"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "EEE"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "EC"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "ME"))
        self.pushButton_3.setText(_translate("MainWindow", "Register"))
        self.label_7.setText(_translate("MainWindow", "Login Form"))
        self.label_8.setText(_translate("MainWindow", "Enter ID"))
        self.label_9.setText(_translate("MainWindow", "Enter Password"))
        self.pushButton_4.setText(_translate("MainWindow", "Login"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Python"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "C/C++"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "Java"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "Php"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "Javascript"))
        self.label_10.setText(_translate("MainWindow", "Choose Subject"))
        self.pushButton_5.setText(_translate("MainWindow", "Submit"))
        self.lineEdit_6.setText(_translate("MainWindow", "Enter Question"))
        self.lineEdit_7.setText(_translate("MainWindow", "Option_1"))
        self.lineEdit_8.setText(_translate("MainWindow", "Option_2"))
        self.lineEdit_9.setText(_translate("MainWindow", "Option_3"))
        self.lineEdit_10.setText(_translate("MainWindow", "Option_4"))
        self.lineEdit_11.setText(_translate("MainWindow", "Answer"))
        self.pushButton_6.setText(_translate("MainWindow", "Insert Question"))
        self.pushButton_7.setText(_translate("MainWindow", "Exit"))
        self.label_11.setText(_translate("MainWindow", "Question..."))
        self.radioButton.setText(_translate("MainWindow", "Option_1"))
        self.radioButton_2.setText(_translate("MainWindow", "Option_2"))
        self.radioButton_3.setText(_translate("MainWindow", "Option_3"))
        self.radioButton_4.setText(_translate("MainWindow", "Option_4"))
        self.pushButton_8.setText(_translate("MainWindow", "Next Question"))
        self.label_12.setText(_translate("MainWindow", "Your Score"))
        self.label_13.setText(_translate("MainWindow", "Total Questions"))
        self.label_14.setText(_translate("MainWindow", "00"))
        self.label_15.setText(_translate("MainWindow", "00"))

        self.pushButton.clicked.connect(self.showLogin)
        self.pushButton_2.clicked.connect(self.showRegister)
        self.pushButton_3.clicked.connect(self.registerUser)
        self.pushButton_4.clicked.connect(self.loginUser)
        self.pushButton_5.clicked.connect(self.submit)
        self.pushButton_6.clicked.connect(self.insertquestion)
       # self.pushButton_7.clicked.connect(self.fetchquestions)


    def homeScreen(self):
        self.frame.hide()

    def showLogin(self):
        self.frame.show()
        self.frame_3.hide()

    def showRegister(self):
        self.frame.show()
        self.frame_2.hide()

    def registerUser(self):
        user = self.comboBox_2.currentText()
        # print(user)
        user_id = self.lineEdit.text()
        user_name = self.lineEdit_2.text()
        user_pwd = self.lineEdit_3.text()
        user_branch = self.comboBox_3.currentText()

        if user == 'Student':
            query = "INSERT INTO students VALUES (%s, %s, %s, %s)"
        elif user == 'Teacher':
            query = "INSERT INTO teachers VALUES (%s, %s, %s, %s)"


        cursor.execute(query, (user_id, user_name, user_pwd, user_branch))



        QMessageBox.about(self, 'Success', 'Inserted Successfully')

    def loginUser(self):
      try:
        user = self.comboBox.currentText()

        user_id = self.lineEdit_4.text()
        user_pwd = self.lineEdit_5.text()

        if user == 'Student':
            query = "SELECT * FROM students "
        else:
            query = "SELECT * FROM teachers "

        cursor.execute(query)
        UserData=cursor.fetchall()
        print(UserData)
        for data in UserData:

          if int(user_id) in data and user_pwd in data:
              print("user exist")
              self.login()
              break
        else:
              QMessageBox.about(self, 'failed', 'login failed')
      except BaseException as ex:
          print(ex)


    def login(self):
              self.frame_3.show()
              self.frame_4.hide()


    def submit(self):
        user = self.comboBox.currentText()
        if user == 'Student':
            self.studentLogin()
        else:
            self.teacherLogin()

    def teacherLogin(self):
        self.frame_4.show()
        self.frame_5.hide()

        self.lineEdit_6.setText("")
        self.lineEdit_7.setText("")
        self.lineEdit_8.setText("")
        self.lineEdit_9.setText("")
        self.lineEdit_10.setText("")
        self.lineEdit_11.setText("")


    def studentLogin(self):
        self.frame_4.show()
        self.frame_6.hide()
        self.fetchall()


    def insertquestion(self):
       try:
         question = self.lineEdit_6.text()
         option1 = self.lineEdit_7.text()
         option2 = self.lineEdit_8.text()
         option3 = self.lineEdit_9.text()
         option4 = self.lineEdit_10.text()
         answer = self.lineEdit_11.text()
         subject=self.comboBox_4.currentText()

         query="INSERT INTO questions VALUES(%s, %s, %s, %s, %s, %s, %s)"
         cursor.execute(query,(question, option1, option2, option3, option4, answer, subject))
         question = QMessageBox.question(self, 'Inserted', 'Insert another question ?', QMessageBox.Yes | QMessageBox.No)
        # print(ques)
         if question == QMessageBox.Yes:
            self.teacherLogin()
         else:
            self.homeScreen()
        #self.settext("")
       except BaseException as ex:
           print(ex)

    def fetchquestion(self):
      try:
         sub = self.comboBox_4.currentText()
         query = "SELECT * FROM questions WHERE subject = %s"
         cursor.execute(query, (sub))
         questions=cursor.fetchall()
         print(questions)
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