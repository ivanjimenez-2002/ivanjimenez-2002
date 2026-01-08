"""
Name: Ivan A. Jimenez Cruz #135089
File: QAbout.py
Description:
The file contains the class that loads the Widget that shows the information in the About section of the program.

"""
# import the PyQt5 tools needed
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)


# class that loads the about ui file
class AboutWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.file = None
        uic.loadUi("QAbout.ui", self)
