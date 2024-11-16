#include <stdio.h>

class Employe{
    public:
        void doNothing();
        virtual int calcularSalario(); 
        explicit Employe(int age1, char* name1, float salary1): age(age1), name(name1), salary(salary1){}


    protected:
        int age;
        char* name; 
        float salary; 
};

class regularEmploye : Employe{
    public:
        int calcularSalario() override; 
    private:
        int daysMissed; 
};

class halfTimeEmploye : Employe{
    public: 
        int calcularSalario() override; 
    private:
        int hoursWorked; 
};

class contractEmploye : Employe{
    public:
        int calcularSalario() override; 
    private:
        int descriptionOfWork; 
};