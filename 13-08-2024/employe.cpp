#include "employe.h"
#include <iostream>

using namespace std; 

int Employe::calcularSalario(){
    return salary; 
}

int regularEmploye::calcularSalario(){
    return (salary - (daysMissed * 100));
}

int halfTimeEmploye::calcularSalario(){
    return (salary * hoursWorked);
}

int contractEmploye::calcularSalario(){
    float total = 0;
    if (descriptionOfWork == 1){
        total = salary * 1.2; 
        return total;
    } 

    else if (descriptionOfWork == 2)
    {
        total = salary * 1.4; 
        return total;
    }
    
    else{
        cout << "The type of work done is not registered yet." << endl; 
        return 1; 
    }
}
