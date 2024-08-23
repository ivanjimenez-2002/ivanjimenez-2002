/*
* CECS 2223, Computer Programming II Laboratory
* Winter 2022, Sec. 05
* Date: January 24, 2023
* Topic: Team Project
* File name: Car.cpp
* Daniel ####, #
* Ivan A. Jimenez Cruz, #135089
* This file defines a class named Car
*/
#include "Car.h"
#include "Dealer.h"

int Car::count = 0;

Car::Car() 
{
	brand = "";
	model = "";
	serialNumber = "";
	count++;
	// Assigns the empty string to all three fields, and
	// increments count by 1
}

Car::Car(string aBrand, string aModel) 
{

	this->brand = aBrand;
	this->model = aModel;
	count++;
	serialNumber = assignSerialNumber();
	


	// The parameterized constructor increments count by 1
	// assigns the brand and model to the fields, and calls
	// the assignSerialNumber method to create the serial number
}
Car::~Car() 
{
	count--;

	cout << "\nThe car " << brand << " " << model << " with serial number " << serialNumber << " has been sold." << endl;

	// The destructor prints the message
	// “The car [brand] [model] with serial number [serial number]
	// has been sold”
}
string Car::assignSerialNumber() 
{
	if (brand != "" && model != "") 
	{
		string tempSerialNumber = "";
		tempSerialNumber += brand.substr(0, 3);
		tempSerialNumber += model.substr(0, 3);
		string strCount = to_string(count);
		cout << strCount;
		int strLenCount = strCount.length();
		for (int i = 0; i < 3 - strLenCount; i++) 
		{
			tempSerialNumber += "0";
		}
		tempSerialNumber += strCount;

		for (int i = 0; i < tempSerialNumber.length(); i++) 
		{
			tempSerialNumber[i] = toupper(tempSerialNumber[i]);
		}

		return tempSerialNumber;
	}
	else 
	{
		return "";
	}

	// assignSerialNumber is a private method which considers
	// the brand, model, and count to create a 9-symbol string.
	// The format is first three letters of the brand, first three 
	// letters of the model and the 3-digit count value
	// If a Toyota Yaris is the first car added, the serial number
	// would be TOYYAR001 // If the brand and model fields have not been assigned a
	// value, the method DOES NOT create a serial number, and  
	// returns the empty string
}

void Car::setBrand(string aBrand) 
{

	if (this->brand == "") 
	{
		this->brand = aBrand;
	}
	// sets brand value IFF not set before
}
void Car::setModel(string aModel) 
{

	if (this->model == "") 
	{
		this->model = aModel;
	}
	// sets model value IFF not set before
}
string Car::getBrand() const 
{
	return brand;
	// If no brand, return empty string
}
string Car::getModel() const 
{
	return model;
	// If no model, return empty string
}
string Car::getSerialNumber() const 
{
	return serialNumber;
	// Returns the empty string if serial number not set
}

	// printCar prints the car’s details in a table-like manner
	// using the format car_brand car_model serial number
	// It uses the parameters as the size of the brand and model
	// fields, and prints N/A if the fields have no value

void Car::printCar(int modelLength, int brandLength) 
{
	if ((modelLength == 0) && (brandLength == 0))
	{
		brand = "N/A";
		model = "N/A";
	}
	cout << left << setw(modelLength) << brand << setw(brandLength) << model << serialNumber << endl;
}