"""
Name: Ivan A. Jimenez Cruz #135089
File: QAddPrisoner.py
Description:
The file contains the class that handles the QAddPrisonerWidget.ui.This class basically grabs the text, date and photo
inserted in the Widget, after this it will change everything to a string data type and pass all this information to the
insert query via the add class created for the purpose to add this information.

"""
# import the PyQt5 tools needed
from Prisoner import Prisoner
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from PyQt5.QtGui import QPixmap
# import the database connection
from DatabaseConnection import DatabaseConnection

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)


# Class that handles the information being inserted to the database
class AddPrisonerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.file = None
        # Loads the corresponding UI file
        uic.loadUi("QAddPrisonerWidget.ui", self)

    # Function that saves the information inserted in the ui file line edits, dates and text edits
    def add_prisoner_clicked(self):
        # connection to the database
        database = DatabaseConnection()

        # saves all the information on the correspond variable
        # on the variables that save the date we first make a variable that takes the date as a QDate type
        # then we make the variable that will save the string to be used by converting the QDate to PyDate type which
        # can in turn be converted to a string
        lastname = self.LastName_lineEdit.text()
        name = self.Name_lineEdit.text()
        bDate = self.Birthdate_dateEdit.date()
        birthDate = str(bDate.toPyDate())
        height = self.Height_lineEdit.text()
        eyes = self.EyeColor_lineEdit.text()
        born = self.Born_lineEdit.text()
        sentence = self.Sentence_textEdit.toPlainText()
        # saves the string form the add_image_clicked function
        photo = self.file
        hair = self.Hair_lineEdit.text()
        dDate = self.DateOfConviction_dateEdit.date()
        dateOfConviction = str(dDate.toPyDate())
        lDate = self.DateToBeLiberated_dateEdit.date()
        dateToBeLiberated = str(lDate.toPyDate())

        # save all the information on a Prisoner data type variable
        prisoner = Prisoner(lastname, name, photo, birthDate, height, hair, eyes, born, sentence, dateOfConviction,
                            dateToBeLiberated)

        # Pass all the information to the add query
        rows, id = database.add(prisoner)

        # always close the database
        database.close()
        # creates a message box
        msgBox = QMessageBox()

        # if statement that saves a message if the information was saved by saying a row was added and the ID created
        if rows == 1:
            msg = f"{rows} record inserted with ID {id}"
        # else send an error message
        else:
            msg = "Database error"

        # set the message on the message box
        msgBox.setText(msg)
        # execute the message box
        msgBox.exec()
        # hide the window
        self.hide()

    # function to handle the information of the photo
    def add_image_clicked(self):
        # opens the files of the computer only showing .jpg files
        imagen = QFileDialog.getOpenFileName(self, "Choose photo", "", "Photos(*.jpg)")
        # saves the file name and direction as a string
        self.file = str(imagen[0])
        # converts the string to a QPixmap data type
        image = QPixmap(imagen[0])
        # sets the photo on the label photo label
        self.foto_label.setPixmap(image)
        # eliminated the direction file and only saves the name (*Name*.jpg)
        self.file = self.file.split('/')[-1]
