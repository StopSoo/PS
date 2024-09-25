#include <iostream>
using namespace std;

int main() {
    int a, b ;

    while (true) {
        cin >> a >> b;
        if (a != 0 && b != 0) {
            if (a % b == a) {   // 첫 번째 숫자가 두 번째 숫자의 약수
                cout << "factor" << endl;
            } else if (a % b == 0) {    // 첫 번째 숫자가 두 번째 숫자의 배수
                cout << "multiple" << endl;
            } else  // 둘 다 아닐 때
                cout << "neither" << endl;
        } else
            break;
    }

    return 0;
}
