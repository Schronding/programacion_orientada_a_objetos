#include <iostream>
#include "triangle.h"

void triangle::setHeight(int hei){
    height = hei;
}

void triangle::setBase(int bas){
    base = bas;
}

void triangle::setArea(int ar){
    area = ar;
}

int triangle::calculateArea(){
    area = (base * height) / 2; 
    return area; 
}

