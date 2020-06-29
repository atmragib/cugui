from functools import partial
import sys
import os
import glob
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout,
                             QApplication, QPushButton)


def calluser(name):
    os.system("gnome-terminal -e 'bash -c \"echo {}; exec bash\"'".format(name))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.lay = QVBoxLayout(self.centralwidget)

        self.btn = QPushButton('{}'.format('refresh'), self)
        text = self.btn.text()
        self.btn.clicked.connect(self.dir_refresh)
        self.lay.addWidget(self.btn)

        names = [os.path.basename(x) for x in glob.glob('./*.cs')]
        names.sort()
        for i in names:
            self.btn = QPushButton('{}'.format(i), self)
            text = self.btn.text()
            self.btn.clicked.connect(partial(calluser, i))
            self.lay.addWidget(self.btn)

    def dir_refresh(self):
        for i in reversed(range(self.lay.count())[1:]):
            layoutItem = self.lay.itemAt(i)
            if layoutItem.widget() is not None:
                widgetToRemove = layoutItem.widget()
                widgetToRemove.setParent(None)
                self.lay.removeWidget(widgetToRemove)
            elif layoutItem.spacerItem() is not None:
                pass
            else:
                layoutToRemove = layout.itemAt(i)
        names = [os.path.basename(x) for x in glob.glob('./*.cs')]
        names.sort()
        for i in names:
            self.btn = QPushButton('{}'.format(i), self)
            text = self.btn.text()
            self.btn.clicked.connect(partial(calluser, i))
            self.lay.addWidget(self.btn)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
