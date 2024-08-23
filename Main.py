"""
Name: Ivan A. Jimenez Cruz #135089
File: Main.py
Description:
The file contains the Driver. This file contains the connection to all the Widgets that are being used in this program.
When they are triggered in the MainWindow the connection happens here. This Driver also contains two functions that
ask for the ID of a prisoner. One function is for to modify and another is for the search.

"""
# import sys
import sys
# import the required PyQt5 tools
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp, QInputDialog, QLineEdit, QMessageBox
# import the classes that handle the ui files
from QAbout import AboutWidget
from QAddPrisoner import AddPrisonerWidget
from QModifyPrisoner import ModifyPrisonerWidget
from QListPrisoners import ListPrisonersWidget
from QViewPrisoner import ViewPrisonerWidget
from Help import HelpWidget

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)


# This is the driver class which executes the whole program
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # load main window
        uic.loadUi("QMainWindowPrisonerDB.ui", self)
        # Connection that when hit Exit on the file section it closes the program
        self.actionExit.triggered.connect(qApp.quit)
        # Assign variables to every class data type that is going to be used
        self.addPrisoner = AddPrisonerWidget()
        self.modifyPrisoner = ModifyPrisonerWidget()
        self.viewPrisoner = ViewPrisonerWidget()
        self.listPrisoners = ListPrisonersWidget()
        self.help = HelpWidget()
        self.about = AboutWidget()
        # connect, executes, shows the class if the action was triggered in the main window
        self.actionAbout.triggered.connect(self.about.show)
        self.actionHelp.triggered.connect(self.help.show)
        self.actionAdd_prisoner.triggered.connect(self.addPrisoner.show)
        self.actionModify_Prisoner.triggered.connect(self.modify_prisoner)
        self.actionSearch_for_a_prisoner.triggered.connect(self.view_prisoner)
        self.actionList_prisoners.triggered.connect(self.listPrisoners.show)

    # function that asks the ID of the prisoner that will be viewed
    def view_prisoner(self):
        # try/except that handles the exception if there is a ValueError
        try:
            # create a box that asks for the ID of the prisoner
            id_str, ok = QInputDialog().getText(self, "Message", "Enter ID:", QLineEdit.Normal, None)
            # if ok of the box id clicked
            if ok:
                # saves the value in id as int
                id = int(id_str)
                # passes the id number to choose_id that will return true if the id is valis
                flag = self.viewPrisoner.choose_id(id)
                # if flag is true it will show the prisoner information
                if flag:
                    self.viewPrisoner.show()
        # except, The ValueError
        except ValueError:
            # Create a message box
            msgBox = QMessageBox()
            # Show message box as critical saying that only numbers are accepted
            msgBox.critical(self, "Error", "Only numbers are accepted", QMessageBox.Ok)

    # function that asks the ID of the prisoner that will be modified
    def modify_prisoner(self):
        # try/except that handles the exception if there is a ValueError
        try:
            # create a box that asks for the ID of the prisoner
            id_str, ok = QInputDialog().getText(self, "Message", "Enter ID:", QLineEdit.Normal, None)
            # if ok of the box id clicked
            if ok:
                # saves the value in id as int
                id = int(id_str)
                # passes the id number to choose_id that will return true if the id is valis
                flag = self.modifyPrisoner.choose_id(id)
                # if flag is true it will show the prisoner information
                if flag:
                    self.modifyPrisoner.show()
        # except, The ValueError
        except ValueError:
            # Create a message box
            msgBox = QMessageBox()
            # Show message box as critical saying that only numbers are accepted
            msgBox.critical(self, "Error", "Only numbers are accepted", QMessageBox.Ok)


# main
def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
