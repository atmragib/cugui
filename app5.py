from PyQt5 import QtCore, QtGui, QtWidgets
import socket
HOST = '192.168.1.33'  # The server's hostname or IP address
PORT = 80              # The port used by the server
 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
 
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)  #pencere boyutu
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 600, 300))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.labelDistance = QtWidgets.QLabel(self.centralwidget)
        self.labelDistance.setGeometry(QtCore.QRect(150, 150, 400, 300))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.labelDistance.setFont(font)
        self.labelDistance.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDistance.setObjectName("labelDistance")
        self.labelcm = QtWidgets.QLabel(self.centralwidget)
        self.labelcm.setGeometry(QtCore.QRect(150, 150, 700, 300))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.labelcm.setFont(font)
        self.labelcm.setAlignment(QtCore.Qt.AlignCenter)
        self.labelcm.setObjectName("labelcm")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 259, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
 
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
 
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Measurement"))
        self.label.setText(_translate("MainWindow", "Distance"))
        self.labelDistance.setText(_translate("MainWindow", data))
        self.labelcm.setText(_translate("MainWindow", "cm"))
         
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())