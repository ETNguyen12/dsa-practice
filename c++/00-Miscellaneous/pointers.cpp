#include <string>
#include <iostream>

using namespace std;

int main() {

    int num1 = 11;
    int num2 = num1;
    num1 = 22;

    cout << "Num 1: " << num1 << endl;
    cout << "Num 2: " << num2 << endl;

    int value = 11;
    int* ptr = &value;
    value = 22;

    cout << "Value: " << value << endl;
    cout << "Pointer: " << *ptr << endl;

    return 0;
}

