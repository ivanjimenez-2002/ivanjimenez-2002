"""
Name: Ivan A. Jimenez Cruz #135089
File: QViewPrisoner.py
Description:
The file contains the class that handles the information for the Search prisoner widget that only shows the information
of a single prisoner. You cannot edit this information in any way.

"""
# import required PyQt5 tools
from PyQt5 import uic
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
# import DatabaseConnection
from DatabaseConnection import DatabaseConnection


QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)


# This class will handle the ui that shows the information of a single prisoner selected bt id nu,ber
class ViewPrisonerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.file = None
        # load ui file
        uic.loadUi("QViewPrisoner.ui", self)

    # Function that sets the text and date in the widgets on the ui file
    def choose_id(self, id):
        # create a connection to the database
        database = DatabaseConnection()
        flag = False
        # execute query by the id passed in the parameter, receives the information of the prisoner
        prisoner = database.select_by_id(id)

        # if statement that makes sure the information received is not empty
        if prisoner is not None:
            flag = True
            # Set all the information to the widgets
            self.ID_lineEdit.setText(str(id))
            self.LastName_lineEdit.setText(prisoner.get_lastName())
            self.Name_lineEdit.setText(prisoner.get_name())
            self.Birthdate_dateEdit.setDate(prisoner.get_birthDate())
            self.Height_lineEdit.setText(str(prisoner.get_height()))
            self.EyeColor_lineEdit.setText(prisoner.get_eyes())
            self.Born_lineEdit.setText(prisoner.get_born())
            self.Sentence_textEdit.setPlainText(prisoner.get_sentence())
            self.foto_label.setPixmap(QPixmap(prisoner.get_photo()))
            self.Hair_lineEdit.setText(prisoner.get_hair())
            self.DateOfConviction_dateEdit.setDate(QDate(prisoner.get_dateOfConviction()))
            # If statement that sets the date to the max date if it receives a NULL
            if prisoner.get_dateToBeLiberated() is None:
                d = QDate(9999, 12, 31)
                self.DateToBeLiberated_dateEdit.setDate(d)
            # else, sets the date to the date to be liberated
            else:
                self.DateToBeLiberated_dateEdit.setDate(QDate(prisoner.get_dateToBeLiberated()))
        # else, nothing was received
        else:
            # create a message box
            msgBox = QMessageBox()
            # set the window title
            msgBox.setWindowTitle("Choose ID")
            # set the text saying that the ID passes was not found
            msgBox.setText(f"ID {id} not found!")
            # execute the message box
            msgBox.exec()
            # Close the database
        database.close()
        return flag