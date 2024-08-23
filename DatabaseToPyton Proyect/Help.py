"""
Name: Ivan A. Jimenez Cruz #135089
File: Help.py
Description:
The file contains the class that loads the Help.ui. The only purpose of this class is to connect this Widget to the
main class so when the help button is triggered on the main window it could load the ui.

"""
# import the PyQt5 tools needed
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)


# class that loads the help ui file
class HelpWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.file = None
        uic.loadUi("QHelp.ui", self)
