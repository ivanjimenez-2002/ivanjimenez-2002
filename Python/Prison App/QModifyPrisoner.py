"""
Name: Ivan A. Jimenez Cruz #135089
File: QModifyPrisoner.py
Description:
The file contains the class that handles the information for the QModifyPrisoner.ui Widget. The class contains two very
important functions: a function that receives and places information of the prisoner selected to the Widget and a
function that saves the information placed in the Widget and saves this information by calling update function which
uses to modify query. It is very important to note that the way I made this class is that right after pushing the
button to save the information the user is obligated to select a photo. This is to assure that every prisoner has a
photo after modifying the prisoner.

"""
# import required PyQt5 tools
from PyQt5 import uic
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from PyQt5.QtGui import QPixmap
# import database connection
from DatabaseConnection import DatabaseConnection
# import Prisoner class
from Prisoner import Prisoner

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)


# This class handles the modify ui file that changes information but also has to take information from the database
class ModifyPrisonerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.file = None
        uic.loadUi("QModifyPrisoner.ui", self)
        # private variable from Prisoner class
        self.__id = -1

    # Function that receives an id number
    def choose_id(self, id):
        # Connect to database
        database = DatabaseConnection()
        # Assign ID passes to id private variable
        self.__id = id
        flag = False
        # Execute the query that takes information from a specific prisoner depending on the id passes as parameter
        prisoner = database.select_by_id(id)

        # is statement that makes sure the information received from the database is not empty
        if prisoner is not None:
            flag = True
            # set all the information passed to their corresponding Widgets
            self.ID_lineEdit.setText(str(id))
            self.LastName_lineEdit.setText(prisoner.get_lastName())
            self.Name_lineEdit.setText(prisoner.get_name())
            self.Birthdate_dateEdit.setDate(prisoner.get_birthDate())
            self.Height_lineEdit.setText(str(prisoner.get_height()))
            self.EyeColor_lineEdit.setText(prisoner.get_eyes())
            self.Born_lineEdit.setText(prisoner.get_born())
            self.Sentence_textEdit.setPlainText(prisoner.get_sentence())
            self.foto_label.setPixmap(QPixmap(prisoner.get_photo()))
            self.modify_label.setText(prisoner.get_photo())
            self.Hair_lineEdit.setText(prisoner.get_hair())
            self.DateOfConviction_dateEdit.setDate(prisoner.get_dateOfConviction())
            if prisoner.get_dateToBeLiberated() is None:
                d = QDate(9999, 12, 31)
                self.DateToBeLiberated_dateEdit.setDate(d)
            # else, sets the date to the date to be liberated
            else:
                self.DateToBeLiberated_dateEdit.setDate(QDate(prisoner.get_dateToBeLiberated()))
        # If there is no information then the ID passes does not have information assigned to it
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

    # Function that saves all the information placed on the Widgets
    # on the variables that save the date we first make a variable that takes the date as a QDate type
    # then we make the variable that will save the string to be used by converting the QDate to PyDate type which
    # can in turn be converted to a string
    def modify_prisoner_clicked(self):
        # Connection to the database
        database = DatabaseConnection()
        # save the information on the Widgets to the corresponding variables
        lastname = self.LastName_lineEdit.text()
        name = self.Name_lineEdit.text()
        bDate = self.Birthdate_dateEdit.date()
        birthDate = str(bDate.toPyDate())
        height = self.Height_lineEdit.text()
        eyes = self.EyeColor_lineEdit.text()
        born = self.Born_lineEdit.text()
        sentence = self.Sentence_textEdit.toPlainText()
        # calls the modify_image to assure that the prisoner has a photo
        self.modify_image()
        # saves the string from the modify_image
        photo = self.file
        hair = self.Hair_lineEdit.text()
        dDate = self.DateOfConviction_dateEdit.date()
        dateOfConviction = str(dDate.toPyDate())
        lDate = self.DateToBeLiberated_dateEdit.date()
        dateToBeLiberated = str(lDate.toPyDate())

        # pass the variables as a Prisoner class data type
        prisoner = Prisoner(lastname, name, photo, birthDate, height, hair, eyes, born, sentence, dateOfConviction,
                            dateToBeLiberated, self.__id)

        # save the information on the row
        rows = database.update(prisoner)
        # close database
        database.close()
        # create as message box
        msgBox = QMessageBox()
        # if the modification was successful
        if rows == 1:
            # create a message saying that the row was updated
            msg = f"{rows} record updated"
        # else send a message that a error occurred
        else:
            msg = "Database error"
        # set the message to the text of the message box
        msgBox.setText(msg)
        # execute the message box
        msgBox.exec()
        self.hide()

    def modify_image(self):
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
