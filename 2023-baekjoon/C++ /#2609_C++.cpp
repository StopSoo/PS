#include <iostream>
using namespace std;

int main() {
    int a, b, min, share_a, share_b, gcd = 1, lcm;
    cin >> a >> b;

    min = (a > b) ? b : a;
    share_a = a; share_b = b;
    // 최대 공약수 구하기
    for (int i=2; i <= min; i++) {
        if (share_a % i == 0 && share_b % i == 0) {
            share_a /= i;
            share_b /= i;
            gcd *= i;   // 최대 공약수
            if (share_a % i == 0) i--;  // 같은 수로 또 나누어진다면
            else continue;
        } else continue;
    }
    // 최소 공배수 구하기
    lcm = (a / gcd) * (b / gcd) * gcd;
    // 출력
    cout << gcd << endl;
    cout << lcm << endl;
    return 0;
}
