
using namespace std; 

class triangle{

    public:
        void setHeight(int hei);
        void setBase(int bas);
        void setArea(int ar); 
        int getHeight();
        int getBase();
        int calculateArea();
        int getArea();

    private: 
        int base;
        int height; 
        int area; 
};