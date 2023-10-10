// #11689 : GCD(n, k) = 1
// GCD(n, k) = 1 ? -> 두 수의 최대 공약수가 1이다 = 두 수가 서로소이다.
// => 오일러 피 함수를 구해라.

// 오일러 피 핵심 이론 부분을 참고해 2~N의 제곱근까지 탐색하면서,
// 소인수일 때 result = result - (result/소인수) 연산으로 result 값을 업데이트한다.
// 이 때 n에서 이 소인수는 나누기 연산으로 삭제한다.

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    // for fast I/O
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    long n;
    cin >> n;
    long result = n;
    // 소인수 분해를 하면 n의 제곱근보다 큰 소인수는 0개 or 1개이다 (!)
    // 그 소인수는 나중에 해결해줄 것이기 때문에, for문은 n의 제곱근까지만 돌린다.
    for (long p = 2; p <= sqrt(n); p++) {
        if (n % p == 0) {   // p가 소인수일 경우
            result = result - (result/p);
            while (n % p == 0)  // 같은 p가 2개 이상으로 중복되었을 경우 대비
                n = n / p;
        }
    }
    // n의 제곱근보다 큰 소인수의 처리
    if (n > 1)
        result = result - (result / n);

    cout << result << "\n";

    return 0;
}