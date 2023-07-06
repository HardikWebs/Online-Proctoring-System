from PyQt5 import QtWidgets, QtGui
from PIL import Image, ImageQt
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import cv2

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 800, 800)
        self.setWindowTitle('Window')
        self.label = QtWidgets.QLabel(self)
        #self.initUI()
        #self.show_cam()

        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            img = Image.fromarray(frame, mode='RGB')
            qt_img = ImageQt.ImageQt(img)
            #self.label = QtWidgets.QLabel(self)
            self.label.setPixmap(QtGui.QPixmap.fromImage(qt_img))
            if cv2.waitKey(1) == ord('q'):
                break
        cap.release()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('My label')
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText('Click')
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText('You pressed the button')
        self.label.adjustSize()

    def show_cam(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            img = Image.fromarray(frame, mode='RGB')
            qt_img = ImageQt.ImageQt(img)
            self.label = QtWidgets.QLabel(self)
            self.label.setPixmap(QtGui.QPixmap.fromImage(qt_img))
            if cv2.waitKey(1) == ord('q'):
                break
        cap.release()

app = QApplication(sys.argv)
win = MyWindow()
win.show()
sys.exit(app.exec_())