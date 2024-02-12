# Main Window
from ..backend.core import generateEmail

import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Generate Email")
        self.text = QtWidgets.QLabel("AI Email Generator v1.0.1" ,
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))


def createWindow():
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())

    destination = "Sergio Madrigal"
    subject = "New SFTP account"
    tone = "Executive Formal"
    content = "The new account has been creared. The new account is saunicoresftp.best. The password is going to be sent through other channel"
    prev = None


    # Create a basic window



    # test = generateEmail(
        # destination, subject, content, tone, prev
    # )

    # return(test)