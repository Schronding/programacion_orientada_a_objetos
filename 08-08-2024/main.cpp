#include <iostream>
#include "triangle.h"
#include <stdio.h>
#include <time.h>

int main(){
    // 
    triangle tris[10];
    int max = -1;
    int index_of_max = -2;

    srand(time(NULL));

    // The loop that generates and stores all the information of the triangles.
    for(int i = 0; i < 10; i++){
        // To set the base and height of each of the triangles
        int base = rand() % 10 + 1;
        int height = rand() % 10 + 1; 
        tris[i].setBase(base);
        tris[i].setHeight(height);

        // To calculate and store the area
        int area = tris[i].calculateArea();
        tris[i].setArea(area);

        // For checking which of all the triangles has the maximum area
        if (area > max){
            max = area;
            index_of_max = i;
        };
    };

    cout << "The maximum area was: " << max << " with the index: " << index_of_max << "\n"; 

    return 0;
};