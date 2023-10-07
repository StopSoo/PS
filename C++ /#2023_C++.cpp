// #2023 : 신기한 소수
// N이 1부터 8까지 : 최댓값이 작다 <=> 시간 복잡도를 고려 안 해도 된다.

// DFS의 재귀 함수 이용해서 풀기 !
// 1. 첫 번째 자릿수는 2,3,5,7에서 시작
// 2. 다음으로 계속 붙이는 자릿수는 홀수만 붙이면 됨 (짝수는 어차피 소수가 안되므로)
//    -> 현재 수 * 10 + a (a : 붙이는 수)

#include <iostream>
using namespace std;

static int N;   // 자릿수를 전역 변수로 선언

bool isPrimeNumber(int number) {
    for (int i = 2; i <= number / 2; i++) {  // 2부터 number/2까지(!) 나누어 떨어지는지 확인
        if (number % i == 0) return false;
    }
    return true;    // 하나도 나누어 떨어지는 수가 없으면 true를 반환
}

void DFS(int number, int pos) {
    // 자릿수가 채워졌을 때
    if (pos == N) {
        if (isPrimeNumber(number))
            cout << number << endl;
        return;
    }
    // 자릿수가 채워지지 않았을 때
    for (int i = 1; i <= 9; i += 2) {   // 뒤에 숫자를 붙여서 DFS 실행
        if (isPrimeNumber(number * 10 + i))
            DFS(number * 10 + i, pos + 1);
    }
}

int main() {
    // for fast I/O
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // 자릿수 입력 받기
    cin >> N;

    // DFS 수행
    // 왼쪽부터 한 자리 수도 소수여야 하므로 2, 3, 5, 7에 대해서만 DFS 수행
    DFS(2, 1);
    DFS(3, 1);
    DFS(5, 1);
    DFS(7, 1);

    return 0;
}