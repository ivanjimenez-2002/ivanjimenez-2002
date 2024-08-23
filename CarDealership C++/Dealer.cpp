/*
* CECS 2223, Computer Programming II Laboratory
* Winter 2022, Sec. 05
* Date: January 24, 2023
* Topic: Team Project
* File name: Dealer.cpp
* Daniel ####, #
* Ivan A. Jimenez Cruz, #135089
* This file defines a class named Dealer
*/
#include "Dealer.h"

Dealer::Dealer() 
{
	count = 0;
	name = "";
	inventory = nullptr;
	brandLength = 0;
	modelLength = 0;
	// initializes numeric fields to 0, name to the
	// empty string, and inventory to the null pointer
}
Dealer::Dealer(string n) 
{
	count = 0;
	name = n;
	inventory = nullptr;
	brandLength = 0;
	modelLength = 0;
	// initializes numeric fields to 0, name to
	// the parameter’s value, and inventory to the null pointer
}
void Dealer::setBrandLength(string brand) 
{
	int length = brand.length() + 2;
	if (length > brandLength) {
		brandLength = length;
	}
}
void Dealer::reduceBrandLength() {
	brandLength = 0;
	for (int i = 0; i < count; i++) 
	{
		int lenght = inventory[i]->getBrand().length() + 2;
		if (lenght > brandLength) 
		{
			brandLength = lenght;
		}
	}
}

void Dealer::setModelLength(string aModel) 
{
	int modelSize = aModel.size() + 2;
	if (modelSize > modelLength) 
	{
		modelLength = modelSize;
	}
}

void Dealer::reduceModelLength()
{
	int maxModelLength = 0;
	for (int i = 0; i < count; i++) 
	{
		int modelSize = inventory[i]->getModel().size();
		if (modelSize > maxModelLength) 
		{
			maxModelLength = modelSize;
		}
	}
	modelLength = maxModelLength + 2;
}

void Dealer::orderInventory()
{
	for (int i = 0; i < count - 1; i++) 
	{
		for (int j = i + 1; j < count; j++) 
		{
			if (inventory[i]->getBrand() > inventory[j]->getBrand()) 
			{
				swap(inventory[i], inventory[j]);
			}
			else if (inventory[i]->getBrand() == inventory[j]->getBrand()) 
			{
				if (inventory[i]->getModel() > inventory[j]->getModel()) 
				{
					swap(inventory[i], inventory[j]);
				}
				else if (inventory[i]->getModel() == inventory[j]->getModel()) 
				{
					if (inventory[i]->getSerialNumber() > inventory[j]->getSerialNumber()) 
					{
						swap(inventory[i], inventory[j]);
					}
				}
			}
		}
	}
}


void Dealer::addCar(string aBrand, string aModel) 
{
	if (aBrand.length() >= 1 && aModel.length() >= 1) 
	{
		Car** newInventory = new Car * [count + 1];
		for (int i = 0; i < count; i++) 
		{
			newInventory[i] = inventory[i];
		}
		newInventory[count] = new Car(aBrand, aModel);
		delete[] inventory;
		inventory = newInventory;
		count++;
		setBrandLength(aBrand);
		setModelLength(aModel);
		orderInventory();
	}
	// Receives a car’s brand and model as parameters. Creates a
	// new Car object and adds it to inventory, increments count,
	// and calls the setModelLength, setBrandLength, and
	// orderInventory methods if brand and model have length >= 2 characters
}
void Dealer::sellCar(string aBrand, string aModel) 
{
	findCar(aBrand, aModel);
	bool carFound = false;
	for (int i = 0; i < count; i++) 
	{
		if (inventory[i]->getBrand() == aBrand && inventory[i]->getModel() == aModel) 
		{
			carFound = true;
			inventory[i]->~Car();
			inventory[i] = inventory[count - 1];
			count--;
			break;
		}
	}
	if (!carFound) 
	{
		cout << "\nCar not found in inventory" << endl;
	}
	// Receives a car’s serial number as parameter. Calls
	// findCar to make sure there is a car with the same serial
	// number in inventory, if not the method ends. If found,
	// removes the car from inventory, decrements count, invokes
	// the Car object’s destructor and calls the
	// reduceModelLength and reduceBrandLength methods.
}
void Dealer::sellCar(string serialNumber) 
{
	int carIndex = findCar(serialNumber);
	if (carIndex == -1) 
	{
		cout << "No car with serial number " << serialNumber << " was found in inventory." << endl;
		return;
	}

	delete inventory[carIndex];
	// Shift all elements after the deleted car one index to the left
	for (int i = carIndex; i < count - 1; i++) 
	{
		inventory[i] = inventory[i + 1];
	}
	count--;
	reduceModelLength();
	reduceBrandLength();
}

void Dealer::findCar(string aBrand, string aModel) const 
{
	bool carFound = false;
	for (int i = 0; i < count; i++) 
	{
		if (inventory[i]->getBrand() == aBrand && inventory[i]->getModel() == aModel) 
		{
			cout << "\nCar found at index " << i + 1 << endl;
			carFound = true;
			break;
		}
	}
	if (!carFound) 
	{
		cout << "\nCar not found in inventory" << endl;
	}
}

int Dealer::findCar(string serialNumber) const 
{
	for (int i = 0; i < count; i++) 
	{
		if (inventory[i]->getSerialNumber() == serialNumber) 
		{
			cout << "\nCar found at index " << i + 1 << endl;
			return i;
		}
	}
	cout << "\nCar not found in inventory" << endl;
	return -1;
}

void Dealer::printBrandInventory() const
{
	if (count == 0)
	{
		return;
	}
	printf("\nDealer %s has %d of cars in inventory:\n", name.c_str(), count);
	printf("%-*s %s\n", brandLength, "BRAND", "COUNT");

	int brandCount[100] = { 0 };
	string brandList[100];
	int uniqueBrand = 0;
	for (int i = 0; i < count; i++) 
	{
		string currentBrand = inventory[i]->getBrand();
		bool brandExist = false;
		for (int j = 0; j < uniqueBrand; j++)
		{
			if (brandList[j] == currentBrand) 
			{
				brandCount[j]++;
				brandExist = true;
				break;
			}
		}
		if (!brandExist) {
			brandList[uniqueBrand] = currentBrand;
			brandCount[uniqueBrand]++;
			uniqueBrand++;
		}
	}

	for (int i = 0; i < uniqueBrand; i++) 
	{
		printf("%-*s %d\n", brandLength, brandList[i].c_str(), brandCount[i]);
	}

	// prints the count of cars per brand. First, it prints the
	// phrase “Dealer [name] has [quantity] of cars in inventory.”
	// It then prints a table with the headers BRAND and COUNT,
	// using brandLength as the size of the BRAND column. If there
	// are no cars in inventory, the table (including the headers)
	// is not printed.
}
void Dealer::printModelInventory() const {
	cout << "\nDealer " << name << " has " << count << " of cars in inventory:" << endl;

	if (count == 0) 
	{
		return;
	}

	printf("%-*s %-*s %s\n", brandLength, "MODEL", modelLength, "BRAND", "COUNT");
	for (int i = 0; i < count; i++)
	{
		string aModel = inventory[i]->getModel();
		string aBrand = inventory[i]->getBrand();
		int counter = 1;
		for (int j = i + 1; j < count; j++) 
		{
			if (inventory[j]->getModel() == aModel && inventory[j]->getBrand() == aBrand) 
			{
				counter++;
			}
		}
		printf("%-*s %-*s %d\n", brandLength, aModel.c_str(), modelLength, aBrand.c_str(), counter);
		i += counter - 1;
	}

	// prints the count of cars per model. First, it prints the
	// phrase “Dealer [name] has [quantity] of cars in inventory.”
	// It then prints a table with the headers BRAND, MODEL, and
	// COUNT, using brandLength as the size of the BRAND column,
	// and modelLength as the size of the MODEL column. If there
	// are no cars in inventory, the table (including the headers)
	// is not printed.
}
void Dealer::printDetailedInventory() const 
{
	cout << "\nDealer " << name << " has " << count << " of cars in inventory:\n" << endl;

	if (count == 0) 
	{
		return;
	}

	printf("%-*s %-*s %s\n", brandLength, "BRAND", modelLength, "MODEL", "Serial Number");
	for (int i = 0; i < count; i++) 
	{
		printf("%-*s %-*s %s\n", brandLength, inventory[i]->getBrand().c_str(), modelLength, inventory[i]->getModel().c_str(), inventory[i]->getSerialNumber().c_str());
	}
}

// Prints a detailed inventory. First, it prints the
// phrase “Dealer [name] has [quantity] of cars in inventory.”
// It then prints a table with the headers BRAND, MODEL, and
// SERIAL NUMBER, using brandLength as the size of the BRAND
// column, and modelLength as the size of the MODEL column.
// If there are no cars in inventory the table (including
// the headers) is not printed.