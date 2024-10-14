###
# Ivan A. Jimenez Cruz
# File: main.py
# This file is the main file. This file contains the menue to manage orders. It uses a while to run until it is said to stop, using user input to decide what task
# will be done
# ###
import Orders

#Menu to decide what actions to take
while True:
    print("\nWelcome to Restaurant Managamnet, enter desired task: ")

    #Input a number to do a certain task
    task = int(input("1 ->Place Order\n2 ->Track Orders\n3 ->Mark as Complete\n4 ->Display orders\n5 ->Show Pending Orders\n6 ->Show Completed Orders\n7 ->Close\nEnter a number: "))
    if (task == 1):
        Orders.place_order()
    elif (task == 2):
        name = input("Enter name to look for order: ")
        Orders.trackOrder(name)
    elif (task == 3):
        name = input("Enter name to complete order: ")
        Orders.markAsComplete(name)
    elif (task == 4):
        Orders.showOrders()
    elif (task == 5):
        Orders.showPendingOrders()
    elif (task == 6):
        Orders.showCompletedOrders()
    elif (task == 7):
        print("Closing...")
        exit()
    else: 
        print("Invalid option...")

