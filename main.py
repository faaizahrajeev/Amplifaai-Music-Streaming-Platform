# Importing PYQT5 methods
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout, QLineEdit
from qtwidgets import PasswordEdit
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from qtpy import QtCore, QtGui, QtWidgets

widgets = {"logo": [], "login": [], "signup": [],
           "backarrow": [], "usernamelabel": [], "passwordlabel": [], "loginusername": [], "loginpass": [],
           "loginBUTT": [],
           "f3backarrow": [], "f3logo": [], "f3user": [], "f3artist": []
           }

# Connecting to MySQL
import mysql.connector
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(user='root', password='ce3t1e7w', host='127.0.0.1',
                                  database='scifaai')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()

# initialise the application, create window widget
# set size, background colour
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("amplifaai - stream music")
window.setFixedWidth(1250)
window.setFixedHeight(750)
window.move(250, 150)
window.setStyleSheet("background: #000000;")

# initialize the grid
grid = QGridLayout()


def remove_widgets():
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()


def switch_to_2():
    remove_widgets()
    frame2()


def switch_to_3():
    remove_widgets()
    frame3()


def switch_to_1():
    remove_widgets()
    frame1()


# login or signup
def frame1():
    # display logo, create a label widget
    # place the image inside it
    logoImage = QPixmap("AMPLIFAAI.png").scaledToWidth(350)
    logo = QLabel()
    logo.setPixmap(logoImage)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    widgets["logo"].append(logo)

    # initilize a button widget and designing
    LOGIN = QPushButton(">  l o g i n  <")
    LOGIN.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    LOGIN.setStyleSheet(
        "*{border: 4px solid '#BC006C';" +
        "border-radius: 35px;" +
        "font-size: 25px;" +
        "color: 'white';" +
        "padding: 18px 0;" +
        "margin: 25px 300px;}" +
        "*:hover{background: '#BC006C';}")
    LOGIN.clicked.connect(switch_to_2)
    widgets["login"].append(LOGIN)

    SIGNUP = QPushButton(">  s i g n u p  <")
    SIGNUP.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    SIGNUP.setStyleSheet(
        "*{border: 4px solid '#BC006C';" +
        "border-radius: 35px;" +
        "font-size: 25px;" +
        "color: 'white';" +
        "padding: 18px 0;" +
        "margin: 25px 300px;}" +
        "*:hover{background: '#BC006C';}")
    widgets["signup"].append(SIGNUP)

    grid.addWidget(widgets["logo"][-1], 0, 0, 1, 2)
    grid.addWidget(widgets["login"][-1], 1, 0, 1, 2)
    grid.addWidget(widgets["signup"][-1], 2, 0, 1, 2)


# login details
def frame3():
    Arrow = QPushButton("")
    Arrow.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    Arrow.setIcon(QtGui.QIcon('double-arrows.png'))
    Arrow.setIconSize(QtCore.QSize(48, 48))
    Arrow.clicked.connect(switch_to_2)
    widgets["backarrow"].append(Arrow)

    usernameLabel = QLabel("username :")
    usernameLabel.setAlignment(QtCore.Qt.AlignCenter)
    usernameLabel.setStyleSheet("""
            QLabel {border-radius: 35px;
                font-family : Times font;
                color: 'white';
                font-size: 35px;
            }
            """)

    passwordLabel = QLabel("password :")
    passwordLabel.setAlignment(QtCore.Qt.AlignCenter)
    passwordLabel.setStyleSheet("""
                QLabel {
                    border-radius: 35px;
                    font-family : Times font;
                    color: 'white';
                    font-size: 35px;
                }
                """)

    usernameboxU = QLineEdit("")
    usernameboxU.setAlignment(QtCore.Qt.AlignCenter)
    usernameboxU.setStyleSheet(
        "*{border: 4px solid '#BC006C';" +
        "border-radius: 35px;" +
        "font-size: 25px;" +
        "color: 'white';" +
        "padding: 18px 0;" +
        "margin: 25px 350px;}" +
        "*:hover{background: '#BC006C';}")

    passwordboxU = QLineEdit()
    passwordboxU.setEchoMode(QLineEdit.Password)
    passwordboxU.setAlignment(QtCore.Qt.AlignCenter)
    passwordboxU.setStyleSheet(
        "*{border: 4px solid '#BC006C';" +
        "border-radius: 35px;" +
        "font-size: 25px;" +
        "color: 'white';" +
        "padding: 18px 0;" +
        "margin: 25px 350px;}" +
        "*:hover{background: '#BC006C';}")

    LOGINbutt = QPushButton(">  l o g i n  <")
    LOGINbutt.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    LOGINbutt.setStyleSheet(
        "*{border-radius: 35px;" +
        "font-size: 30px;" +
        "color: 'white';" +
        "padding: 18px 0;" +
        "margin: 25px 450px;}" +
        "*:hover{background: '#BC006C';}")

    widgets["loginBUTT"].append(LOGINbutt)
    widgets["backarrow"].append(Arrow)
    widgets["loginusername"].append(usernameboxU)
    widgets["loginpass"].append(passwordboxU)
    widgets["usernamelabel"].append(usernameLabel)
    widgets["passwordlabel"].append(passwordLabel)

    grid.addWidget(widgets["backarrow"][-1], 0, 1)
    grid.addWidget(widgets["usernamelabel"][-1], 2, 0, 1, 2)
    grid.addWidget(widgets["loginusername"][-1], 3, 0, 1, 2)
    grid.addWidget(widgets["passwordlabel"][-1], 4, 0, 1, 2)
    grid.addWidget(widgets["loginpass"][-1], 5, 0, 1, 2)
    grid.addWidget(widgets["loginBUTT"][-1], 6, 0, 1, 2)


# user or artist
def frame2():
    Arrow = QPushButton("")
    Arrow.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    Arrow.setIcon(QtGui.QIcon('double-arrows.png'))
    Arrow.setIconSize(QtCore.QSize(48, 48))
    Arrow.clicked.connect(switch_to_1)

    widgets["f3backarrow"].append(Arrow)

    # display logo, create a label widget
    # place the image inside it
    logoImage = QPixmap("AMPLIFAAI.png").scaledToWidth(350)
    logo = QLabel()
    logo.setPixmap(logoImage)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    widgets["f3logo"].append(logo)

    # initilize a button widget and designing
    USER = QPushButton(">  u s e r  <")
    USER.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    USER.setStyleSheet(
        "*{border: 4px solid '#BC006C';" +
        "border-radius: 35px;" +
        "font-size: 25px;" +
        "color: 'white';" +
        "padding: 18px 0;" +
        "margin: 25px 300px;}" +
        "*:hover{background: '#BC006C';}")
    USER.clicked.connect(switch_to_3)
    widgets["f3user"].append(USER)

    ARTIST = QPushButton(">  a r t i s t  <")
    ARTIST.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    ARTIST.setStyleSheet(
        "*{border: 4px solid '#BC006C';" +
        "border-radius: 35px;" +
        "font-size: 25px;" +
        "color: 'white';" +
        "padding: 18px 0;" +
        "margin: 25px 300px;}" +
        "*:hover{background: '#BC006C';}")
    ARTIST.clicked.connect(switch_to_3)
    widgets["f3artist"].append(ARTIST)

    grid.addWidget(widgets["f3backarrow"][-1], 0, 1)
    grid.addWidget(widgets["f3logo"][-1], 1, 0, 1, 2)
    grid.addWidget(widgets["f3user"][-1], 2, 0, 1, 2)
    grid.addWidget(widgets["f3artist"][-1], 3, 0, 1, 2)


frame1()

window.setLayout(grid)

# show the window
window.show()
sys.exit(app.exec())
