// #1931 : 회의실 배정
// 1. 현재 회의의 종료 시간이 빠를 수록 다음 회의와 겹치지 않게 시작하는 데 유 => 종료 시간이 빠른 순서대로 정렬
// 2. 종료 시간이 같을 때는 시작 시간을 기준으로 다시 한 번 정렬할 것 (중요!)
// 3. 이미 종료 시간이 빠른 순서로 정렬해놨기 때문에, 차례대로 탐색하다가 시간이 겹치지 않는 회의가 나오면 선택한다.

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    // for fast I/O
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    // 회의 개수 입력 받기
    int N;
    cin >> N;
    // 회의 시작 시간, 종료 시간을 배열에 저장
    vector<pair<int, int>> A(N);
    for (int i = 0; i < N; i++) {
        // 종료 시간이 우선순위가 높기 떄문에 종료 시간을 first로 받는다. (정렬의 우선 순위 고려)
        cin >> A[i].second; // 시작 시간
        cin >> A[i].first;  // 종료 시간
    }
    // 정렬
    sort(A.begin(), A.end());

    int count = 0;
    int end = -1;   // 시작 시간과 끝나는 시간이 2^31-1보다 작거나 같은 자연수 또는 0이기 때문

    for (int i = 0; i < N; i++) {
        if (A[i].second >= end) {   // 현재 회의의 시작 시간이 가장 최근 회의의 종료 시간보다 같거나 크다면
            end = A[i].first;   // 종료 시간을 현재 회의의 종료 시간으로 변경
            count++;    // 가능한 회의 개수 카운트
        }
    }

    cout << count << "\n";
    return 0;
}