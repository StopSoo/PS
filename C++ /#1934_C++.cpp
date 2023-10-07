#include <iostream>
using namespace std;

// 최대 공약수 구하는 함수 (유클리드)
int gcd (int a, int b) {
    int c = a % b;
    while (c != 0) {
        a = b;
        b = c;
        c = a % b;
    }
    return b;
}
// 최소 공배수를 구하는 함수
int lcm(int a, int b) {
    return (a * b) / gcd(a, b);
}

int main() {
    int case_num;
    cin >> case_num;
    int n1, n2;
    for (int i=0; i < case_num; i++) {
        cin >> n1 >> n2;
        cout << lcm(n1, n2) << endl;
    }

    return 0;
}
