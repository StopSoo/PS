// #10989 : 수 정렬하기 3
// N의 최댓값이 10,000,000으로 매우 크기 때문에 O(nlogn)보다 더 빠른 알고리즘 필요
// 숫자의 크기가 10,000 이하라는 것(매우 작음)을 바탕으로 계수 정렬(counting sort)를 사용하여 문제를 해결할 것.

// 제약 조건
// 1. 데이터가 양수여야 함.
// 2. 데이터 하나 하나 값들이 매우 작아야 함.

#include <iostream>
using namespace std;

int main() {
    // for more fast I/O
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;
    int count[10001] = {0};   // 최대 10000까지인데 인덱스를 1부터 사용할 것이므로 10001의 크기로 선언
    int number;

    for (int i = 1; i <= N; i++) {
        cin >> number;  // 배열의 수를 하나씩 받기
        count[number]++;    // 해당 수의 인덱스 원소의 값을 1 증가시키기
    }

    for (int i = 1; i <= 10000; i++) {
        if (count[i] != 0) {    // 계수가 0이 아닐 때만 출력
            for (int j = 0; j < count[i]; j++)  // 해당 수를 체크한 계수 만큼 출력
                cout << i << "\n";
        }
    }

    return 0;
}
