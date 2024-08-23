"""
Name: Ivan A. Jimenez Cruz #135089
File: Prisoner.py
Description:
The file contains the Prisoner class which handles the variables of each item that is saved in the database. Each item
has a getter and a setter. The class also has a function that returns all the values saved in each variable and a
function that sets a value to each of the variables. Each one is used in the queries to help handle the information
easier.

"""


class Prisoner:
    # Constructor with parameters
    def __init__(self, lastName="", name="", photo="", birthDate="", height=0.0, hair="", eyes="", born="",
                 sentence="", dateOfConviction="", dateToBeLiberated="", id=-1):
        self.__id = id
        self.__name = name
        self.__lastName = lastName
        self.__photo = photo
        self.__birthDate = birthDate
        self.__height = height
        self.__hair = hair
        self.__eyes = eyes
        self.__born = born
        self.__sentence = sentence
        self.__dateOfConviction = dateOfConviction
        self.__dateToBeLiberated = dateToBeLiberated

    # Setters
    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_lastName(self, lastName):
        self.__lastName = lastName

    def set_birthDate(self, birthDate):
        self.__birthDate = birthDate

    def set_height(self, height):
        # Exception handling
        if isinstance(height, int):
            self.__height = height
        else:
            raise ValueError("The height must be a number!!")

    def set_eyes(self, eyes):
        self.__eyes = eyes

    def sey_hair(self, hair):
        self.__hair = hair

    def set_born(self, born):
        self.__born = born

    def set_sentence(self, sentence):
        self.__sentence = sentence

    def set_dateOfConviction(self, dateOfConviction):
        self.__dateOfConviction = dateOfConviction

    def set_dateToBeLiberated(self, dateToBeLiberated):
        self.__dateToBeLiberated = dateToBeLiberated

    def set_photo(self, photo):
        self.__photo = photo

    # Getters
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_lastName(self):
        return self.__lastName

    def get_birthDate(self):
        return self.__birthDate

    def get_height(self):
        return self.__height

    def get_hair(self):
        return self.__hair

    def get_eyes(self):
        return self.__eyes

    def get_born(self):
        return self.__born

    def get_sentence(self):
        return self.__sentence

    def get_dateOfConviction(self):
        return self.__dateOfConviction

    def get_dateToBeLiberated(self):
        return self.__dateToBeLiberated

    def get_photo(self):
        return self.__photo

    # special getter that returns all the variables at once
    def get_update_values(self):
        return self.__lastName, self.__name, self.__photo, self.__birthDate, self.__height, self.__hair, self.__eyes, \
            self.__born, self.__sentence, self.__dateOfConviction, self.__dateToBeLiberated, self.__id

    # special setter that sets all the variables at once
    def get_insert_values(self):
        return self.__lastName, self.__name, self.__photo, self.__birthDate, self.__height, self.__hair, self.__eyes, \
            self.__born, self.__sentence, self.__dateOfConviction, self.__dateToBeLiberated
