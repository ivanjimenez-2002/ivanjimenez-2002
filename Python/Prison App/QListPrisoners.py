"""
Name: Ivan A. Jimenez Cruz #135089
File: QListPrisoners.py
Description:
The file contains the class that handles the QListPrisoners.ui. This class will access the select all query which
fetches all the information in the database. All this information is then organized in a tableWidget.

"""
# import required PyQt5 tools
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QWidget
# import the database connection class to use all the functions needed
from DatabaseConnection import DatabaseConnection

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)


# Class that handles the tabular view of the prisoners
class ListPrisonersWidget(QWidget):
    def __init__(self):
        super().__init__()
        # Loads the desired ui file
        uic.loadUi("QListPrisoners.ui", self)

        # creates a database connection
        database = DatabaseConnection()

        # assigns the function that selects all prisoners from the database
        all_prisoners_cursor = database.select_all_prisoners()
        # assigns the tableView Widget used in the ui file
        tableWidget = self.Prisoner_tableView

        # Lets any data passed to be shown on the table
        model = QStandardItemModel()
        # Creating the header
        model.setHorizontalHeaderLabels(['ID', 'Last Name', 'Name', 'Photo File', 'Birth Date', 'Height', 'Hair',
                                         'Eyes', 'Place Of Birth', 'Sentence', 'Date of conviction',
                                         'Date of Liberation'])

        # Row count will be zero since the table is empty
        row = 0

        # for loop to save all the information received from the select all query in a respective variable in an array
        for (id, lastName, name, photo, birthDate, height, hair, eyes, born, sentence, dateOfConviction,
             dateOfLiberation) in all_prisoners_cursor:

            array_data = [str(id), lastName, name, photo, str(birthDate), str(height), hair, eyes, born, sentence,
                          str(dateOfConviction), str(dateOfLiberation)]

            # for loop to set a row with the information that corresponds to it
            for column in range(12):
                item = QStandardItem()
                # saves the value from the array
                value = array_data[column]
                # sets the value on a cell
                item.setData(value, Qt.DisplayRole)
                # sets the item on its corresponding row
                model.setItem(row, column, item)
            # adds a row after one prisoner is added to add another one
            row = row + 1

        # sets all the information in the tableWidget
        tableWidget.setModel(model)
        # close the database
        database.close()
