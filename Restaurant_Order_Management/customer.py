###
# Ivan A. Jimenez Cruz
# File: customer.py
# This file contains the Customer class, this will hold the customer's information: Name, Total and Status. The class will also control how variables are extracted 
# and changed. The class will also contain a function to print the customer info in a specific format and will calculate a new total with tip. 
# ###

class Customer:
    def __init__(self):
        self.name = ""
        self.total = 0.00
        self.status = ""

    def setCustomer(self, name, total, status):
        self.name = name
        self.total = total
        self.status = status

    def getName(self):
        return self.name
    
    def setName(self, new_name):
        self.name = new_name
    
    def getTotal(self):
        return self.total
    
    def setTotal(self, new_total):
        self.total = new_total
    
    def getStatus(self):
        return self.status
    
    def setStatus(self, status):
        self.status = status
    
    def changeStatus(self):
        status = self.getStatus()
        if status == "Pending":
            self.setStatus("Completed")
        elif status == "Completed":
            self.setStatus("Pending")

    def printCustomer(self):
        print(f"Name: {self.getName()}, Total: ${self.getTotal()}, Status: {self.getStatus()}")

    def calculateTip(self, tip):
        if tip != 0:
            tip = tip*(10**-2)
            total = self.getTotal()
            new_total = round(total * tip, 2)
            new_total = round(total + new_total, 2)
            self.setTotal(new_total)
