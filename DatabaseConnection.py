"""
Name: Ivan A. Jimenez Cruz #135089
File: DatabaseConnection.py
Description:
The file contains the connection to the SQL database. The cursor is created as well as all the queries: select all data,
select by id, insert and modify. Each one has a function made, so it's the function that accesses the queries on all the
other classes. Queries also have to be executed when told so which the function does as well. It is very important to
note that everytime all these functions are called the database is opened, so everytime they are called the database
is closed afterwards.

"""
# imports sql connectors and Errors in the database
from mysql.connector import Error
import mysql.connector as connection

# import the Prisoner class to use his functions
from Prisoner import Prisoner


class DatabaseConnection:
    def __init__(self):
        # create a database cursor
        self.cursor = None

        # initiate a try/except in case an error has occurred while connecting the database and creating the queries
        try:
            # connection to the database established
            self.database = connection.connect(
                host="####",
                user="####",
                password="####",
                database="####"
            )

            # Query to select all the information in the database
            self.select_all_query = "SELECT * FROM Prison"

            # Query to select the information of an ID passes
            self.select_by_id_query = "SELECT * FROM Prison where prisonerID = %s"

            # Query to insert information received, string for dates have to be converted to a date data type
            self.insert_query = "INSERT INTO Prison (lastname, firstName, photo, birthDate, height, hair, eyes, " \
                                "placeOfBirth, sentence, dateOfConviction, dateToBeLiberated) values (%s, %s, %s, " \
                                "STR_TO_DATE(%s, '%Y-%m-%d'), %s, %s, %s, %s, %s, " \
                                "STR_TO_DATE(%s, '%Y-%m-%d'), STR_TO_DATE(%s, '%Y-%m-%d'))"

            # Query to update the information in the database
            self.update_query = "UPDATE Prison set lastname=%s, firstName=%s, photo=%s, birthDate=%s, height=%s, " \
                                "hair=%s, eyes=%s, placeOfBirth=%s, sentence=%s, dateOfConviction=%s, " \
                                "dateToBeLiberated=%s where prisonerID=%s"

            # cursor variables set as the database cursor
            self.cursor = self.database.cursor()

        # Except
        except Error as e:
            print(e)

    # Function created to receive the information to be added and executing the insert query
    def add(self, prisoner):
        self.cursor.execute(self.insert_query, prisoner.get_insert_values())
        self.database.commit()

        # returns the rowcount and add a value to ID
        return self.cursor.rowcount, self.cursor.lastrowid

    # Function created to execute the select all query
    def select_all_prisoners(self):
        self.cursor.execute(self.select_all_query)

        # returns all the information in the database
        return self.cursor

    # Function that receives an int as the ID number and executed the select by id query which grabs the information of
    # the ID passed
    def select_by_id(self, id):
        prisoner = None
        # value takes the value of id
        values = (id,)

        # database cursor executes the select by id query passing the value of the ID
        self.cursor.execute(self.select_by_id_query, values)
        # results saves all the information
        results = self.cursor.fetchall()

        # if statement that checks the length of results is not zero and there is actually information
        if len(results) > 0:
            # for loop that saves the information on the corresponding variable, goes one by one
            for record in results:
                id, lastname, name, photo, birthDate, height, hair, eyes, born, sentence, dateOfConviction, \
                    dateOfLiberation = record
                # creates a Prisoner data type variable that passes the information previous saved to initialize the
                # variables in the class
                prisoner = Prisoner(lastname, name, photo, birthDate, height, hair, eyes, born, sentence,
                                    dateOfConviction, dateOfLiberation, id)
        # returns all the information in the variable
        return prisoner

    # Function to update information in a prisoner
    def update(self, prisoner):
        self.cursor.execute(self.update_query, prisoner.get_update_values())
        self.database.commit()

        return self.cursor.rowcount

    # Function created to close the database everything it is opened to get information from it
    def close(self):
        self.cursor.close()
        self.database.close()

#Databse Setup

# CREATE DATABASE PrisonDB;
# USE PrisonDB;
#
# Create Table Prison (
#     prisonerID int auto_increment not null,
#     lastName varchar(25),
#     firstName varchar(25),
#     photo varchar(25),
#     birthDate date,
#     height decimal,
#     hair varchar(15),
#     eyes varchar(15),
#     placeOfBirth varchar(15),
#     sentence varchar(255),
#     dateOfConviction date,
#     dateToBeLiberated date,
#     unique(prisonerID)
# );
#
# insert into Prison
# values (null, 'Manson', 'Charles', 'cmanson.jpg', '1934-11-12', 5.7, 'black', 'black', 'USA',
#         'Commuted to life imprisonment without the possibility of parole', '1951-10-01', null);
#
# Select * from Prison;

