/*
* CECS 2223, Computer Programming II Laboratory
* Winter 2022, Sec. 05
* Date: January 24, 2023
* Topic: Team Project
* File name: Car.h
* Daniel ####, #
* Ivan A. Jimenez Cruz, #135089
* This file declares a class named Car
*/
#pragma once
#include <string>
#include <iostream>
#include <iomanip>
using namespace std;

class Car {
private:
    static int count;
    string brand;
    string model;
    string serialNumber;
    string assignSerialNumber();

public:
    Car();
    Car(string brand, string model);
    ~Car();
    void setBrand(string);
    void setModel(string);
    string getBrand() const;
    string getModel() const;
    string getSerialNumber() const;
    void printCar(int, int);
};