#include <iostream>

using namespace std;

class Cookie {
    private:
        string color;

    public:
        Cookie (string color) {
            this->color = color;
        }
        string getColor () {
            return this->color;
        }
        void setColor (string color) {
            this->color = color;
        }
};

int main () {
    Cookie* cookieOne = new Cookie("green");
    Cookie* cookieTwo = new Cookie("blue");

    cout << "C1: " << cookieOne->getColor() << endl;
    cout << "C2: " << cookieTwo->getColor() << endl << endl;

    cout << "Set new colors" << endl;
    cookieOne->setColor("red");
    cookieTwo->setColor("white");

    cout << "C1: " << cookieOne->getColor() << endl;
    cout << "C2: " << cookieTwo->getColor() << endl;

    return 0;
};