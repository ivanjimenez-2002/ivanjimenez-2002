/*
* CECS 2223, Computer Programming II Laboratory
* Winter 2022, Sec. 05
* Date: January 24, 2023
* Topic: Team Project
* File name: Dealer.h
* Daniel ####, #
* Ivan A. Jimenez Cruz, #135089
* This file declares a class named Dealer
*/
#pragma once
#include <iostream>
#include <string>
#include <iomanip>
#include "Car.h"

class Dealer {
private:
    int count; // The number of cars in inventory
    string name;
    Car** inventory;
    int brandLength;
    void setBrandLength(string);
    void reduceBrandLength();
    int modelLength;
    void setModelLength(string);
    void reduceModelLength();
    void orderInventory();

public:
    Dealer();
    Dealer(string);
    void addCar(string, string);
    void sellCar(string, string);
    void sellCar(string);
    void findCar(string, string) const;
    int findCar(string) const;
    void printBrandInventory() const;
    void printModelInventory() const;
    void printDetailedInventory() const;
};