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
           "loginBUTT": []
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

    grid.addWidget(widgets["logo"][-1], 0, 0)
    grid.addWidget(widgets["login"][-1], 1, 0)
    grid.addWidget(widgets["signup"][-1], 2, 0)


def frame2():
    Arrow1 = QPixmap("double-arrows.png").scaledToWidth(50)
    Arrow = QLabel()
    Arrow.setWordWrap(True)
    Arrow.setPixmap(Arrow1)
    Arrow.setAlignment(QtCore.Qt.AlignLeft)
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
        "margin: 25px 400px;}" +
        "*:hover{background: '#BC006C';}")

    widgets["loginBUTT"].append(LOGINbutt)
    widgets["backarrow"].append(Arrow)
    widgets["loginusername"].append(usernameboxU)
    widgets["loginpass"].append(passwordboxU)
    widgets["usernamelabel"].append(usernameLabel)
    widgets["passwordlabel"].append(passwordLabel)

    grid.addWidget(widgets["backarrow"][-1], 0, 0)
    grid.addWidget(widgets["usernamelabel"][-1], 2, 0)
    grid.addWidget(widgets["loginusername"][-1], 3, 0)
    grid.addWidget(widgets["passwordlabel"][-1], 4, 0)
    grid.addWidget(widgets["loginpass"][-1], 5, 0)
    grid.addWidget(widgets["loginBUTT"][-1], 6, 0)

frame2()
window.setLayout(grid)

# show the window
window.show()
sys.exit(app.exec())
