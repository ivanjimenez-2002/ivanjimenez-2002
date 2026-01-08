/*
* CECS 2223, Computer Programming II Laboratory
* Winter 2022, Sec. 05
* Date: January 24, 2023
* Topic: Team Project
* File name: finalProject.cpp
* Daniel ####, #
* Ivan A. Jimenez Cruz, #135089
* This file implements a class named Car and a class named Dealer
*/
#include"Dealer.h" 

int menu() {

    int selection = 0;

    do
    {
        cout << "\nSelect one of the following: " << endl;
        cout << "\t1. Add a car to inventory" << endl;
        cout << "\t2. Sell a car from inventory" << endl;
        cout << "\t3. Find a car by brand and model" << endl;
        cout << "\t4. Find a car by serial number" << endl;
        cout << "\t5. Print the brand inventory" << endl;
        cout << "\t6. Print the model inventory" << endl;
        cout << "\t7. Print the detailed inventory" << endl;
        cout << "\t8. Exit the application" << endl;
        cout << "\n\tEnter option: ";
        cin >> selection;
    } while (selection < 1 || selection > 8);
    return selection;
}
/*int execute(int option, Dealer poli);
{

    do {
        option = menu();
        switch (option) {
        case 1: //add a car to inventory
            cin.ignore(256, '\n');
            cout << "Enter the car's brand: ";
            getline(cin, brand);
            cout << "Enter the car's model: ";
            getline(cin, model);
            poli.addCar(brand, model);
            cout << endl;
            break;
        case 2: //Sell a car from inventory
            cin.ignore(256, '\n');
            cout << "Enter the car's brand: ";
            getline(cin, brand);
            cout << "Enter the car's model: ";
            getline(cin, model);
            poli.sellCar(brand, model);
            break;
        case 3://Find a car by brand and model
            cin.ignore(256, '\n');
            cout << "Enter the car's brand: ";
            getline(cin, brand);
            cout << "Enter the car's model: ";
            getline(cin, model);
            poli.findCar(brand, model);
            break;
        case 4: // find car serialnumber
            cin.ignore(256, '\n');
            cout << "Enter the car's serial number: ";
            getline(cin, serial);
            poli.findCar(serial);
            break;
        case 5:
            poli.printBrandInventory();
            break;
        case 6:
            poli.printModelInventory();
            break;
        case 7:
            poli.printDetailedInventory();
            break;
        case 8:
            cout << "\nProgram Developed by Ivan A. Jimenez Cruz, ID#135089 and Daniel #\n";
            cout << "\nClosing application...";
            break;
        default:
            cout << "Invalid selection, please try again." << endl;
            break;
        }
    } while (option != 8);

    return 0;
}*/

int main() {
    Dealer poli("Poli Auto Sales");
    string brand;
    string model;
    string serial;
    int option = 0;
    do {
        option = menu();
        switch (option) {
        case 1: //add a car to inventory
            cin.ignore(256, '\n');
            cout << "Enter the car's brand: ";
            getline(cin, brand);
            cout << "Enter the car's model: ";
            getline(cin, model);
            poli.addCar(brand, model);
            cout << endl;
            break;
        case 2: //Sell a car from inventory
            cin.ignore(256, '\n');
            cout << "Enter the car's brand: ";
            getline(cin, brand);
            cout << "Enter the car's model: ";
            getline(cin, model);
            poli.sellCar(brand, model);
            break;
        case 3://Find a car by brand and model
            cin.ignore(256, '\n');
            cout << "Enter the car's brand: ";
            getline(cin, brand);
            cout << "Enter the car's model: ";
            getline(cin, model);
            poli.findCar(brand, model);
            break;
        case 4: // find car serialnumber
            cin.ignore(256, '\n');
            cout << "Enter the car's serial number: ";
            getline(cin, serial);
            poli.findCar(serial);
            break;
        case 5:
            poli.printBrandInventory();
            break;
        case 6:
            poli.printModelInventory();
            break;
        case 7:
            poli.printDetailedInventory();
            break;
        case 8:
            cout << "\nProgram Developed by Ivan A. Jimenez Cruz, ID#135089 and Daniel Montes Torres #142281\n";
            cout << "\nClosing application...\n";
            break;
        default:
            cout << "Invalid selection, please try again." << endl;
            break;
        }
    } while (option != 8);
    //while (execute(menu(), poli));
    system("pause"); // Visual Studio only!
    return 0;
}
