# Importing PYQT5 methods
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

widgets= {"logo": [],
          "login": [],
          "signup": []
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

frame1()

window.setLayout(grid)

# show the window
window.show()
sys.exit(app.exec())
