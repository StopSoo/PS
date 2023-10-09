// #1456 : 거의 소수

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    // for fast I/O
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    long min, max;
    cin >> min >> max;
    long A[10000001];

    // 소수 구하기
    for (int i = 2; i < 10000001; i++) A[i] = i;    // 1차 초기화
    for (int i = 2; i < sqrt(10000001); i++) {
        if (A[i] == 0) continue;    // 소수가 아니면 패스
        for (int j = i * 2; i < 10000001; j += i) A[j] = 0; // 소수라면 i의 배수를 돌면서 0으로 체크
    }

    int count = 0;  // 거의 소수의 개수
    // 거의 소수 구하기
    for (int i = 2; i < 10000001; i++) {
        if (A[i] != 0) {
            long temp = A[i];
            // 이항정리를 이용해서 이렇게 작성하는 게 중요(!)
            while ((double)A[i] <= (double)max/(double)temp) {
                if ((double)A[i] >= (double)min/(double)temp) {
                    count++;
                }
                temp *= A[i];
            }
        }
    }
    // 출력
    cout << count << "\n";
    return 0;
}