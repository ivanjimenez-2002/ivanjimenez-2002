###
# Ivan A. Jimenez Cruz
# File: Orders.py
# This file controls everyting, this file controls all functions that where asked for and are the ones called in the main function. This file holds a list of Customer
# objects that uses the class function to get and use information.  
# ###
from customer import Customer

#List that will contain all customer orders
orders = []

#Dictionary that holds the item and price B = Burger, F = Fries, D = Drink, S = Salad 
items = {'B':5.99, 'F':2.99, 'D':1.99, 'S':4.99 }

#Contains all the charecters that keys form the dictionary to use in the function
legend = ['B', 'F', 'D', 'S']

#function called from main to place order and save it in orders
def place_order():
    value = 0.0  #Initialize value variable to 0.0, this will hold the total of the customer
    print("Food Legend: B = Burger, F = Fries, D = Drink, S = Salad...E to exit\n")
    name = input("Name of Customer: ") #save customer name

    #Run through the list to chack if there is already an order with the same name
    for obj in orders:
         while True:
            if obj.getName() == name:
                #If true, change the name, it will loop until the name is changed
                name = input("Name already used, enter another or add full name: ")
            else:
                break

    print("What will be the order?\n")

    #While the charecter entered id not E (Exit) loop around again to keep adding to the order
    while True:
        item = input("Place item charecter: ").upper() #Prevent case sensitivity
        #Check if the charecter is E to exit
        if(item == 'E'):
            print("Order Placed...Exiting...")
            break
        #Check that the charecter is in legend (Error Handling)
        if item in legend:
            value += items.get(item)
        else: 
            wrong = True
            while wrong == True:
                item = input("Charecter not valid, entrer again: ")
                if item in legend:
                 value += items.get(item)
                 wrong = False
        customer = Customer()
        customer.setCustomer(name, value, "Pending")
    
    #Save the order to the list
    orders.append(customer)
    print(f"Order saved for {customer.getName()}. Total: ${customer.getTotal()}")

#Function that will exclusively look for Completed orders
def showCompletedOrders():
    order = False
    #Look for orders that have a Completed Status
    for obj in orders:
        if obj.getStatus() == "Completed":
            obj.printCustomer()
            order = True
        
    if order == False:
        print("\nNo Completed Orders!\n")

#Function that will exclusivley look for Pendig Orders
def showPendingOrders():
    order = False
    #Look for orders that have a Pending Status
    for obj in orders:
        if obj.getStatus() == "Pending":
            obj.printCustomer()
            order = True

    if order == False:
        print("\nNo Pending Orders!\n")
    

#Create a function that will print all the orders
def showOrders():
    order = False
    #Print the orders list
    for obj in orders:
        obj.printCustomer()
        order = True

    if order == False:
        print("\nNo Orders!\n")
    
#Make a function to change the status of an order
def markAsComplete(name):
    for obj in orders:
        if obj.getName() == name:
            print("\nDo you want o leave a tip?\n")
            tip = int(input("Enter percent number: "))
            obj.calculateTip(tip)
            obj.changeStatus()
            print(f"Order from {obj.getName()} marked as complete. Total of ${obj.getTotal()}")

#Make a function thet will track a specific order
def trackOrder(name):
    for obj in orders:
        if name == obj.getName():
            print(f"Order from {name}\nTotal: ${obj.getTotal()}\nStatus: {obj.getStatus()}")
            break
        else:
            print(f"Order with name {name} was not found...")
