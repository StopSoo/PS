// 백준 #1377
// N이 500,000보다 작거나 같은 자연수 -> N^2의 시간 복잡도를 갖는 버블 정렬로 풀 수 X, NlogN의 시간 복잡도로 풀어야 함
// 아이디어 ) 특정 데이터가 안쪽 루프에서 swap을 통해 왼쪽으로 이동할 수 있는 최대 거리가 1임.
//         데이터의 정렬 전 index와 정렬 후 index를 비교해서 왼쪽으로 가장 많이 이동한 값을 찾으면 이 문제를 해결할 수 있다.

// 풀이법
// 1. 기본으로 제공하는 sort() 함수로 배열을 정렬 (sort() 함수는 시간 복잡도가 nlogn임)
// 2. 각 데이터마다 정렬 전 index 값에서 정렬 후 index 값을 빼고 최댓값을 찾음.
// 3. 그리고 swap이 일어나지 않는 반복문이 한 번 더 실행되는 것을 감안해 최댓값에 1을 더함.

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    // for more fast I/O
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;
    vector<pair<int, int>> A(N);    // index와 value를 같이 저장

    for (int i = 0; i < N; i++) {
        cin >> A[i].first;  // 배열 값
        A[i].second = i;    // 배열의 index
    }

    sort(A.begin(), A.end());   // 정렬

    int Max = 0;
    for (int i = 0; i < N; i++) {
        if (Max < A[i].second - i) {    // 배열 원소들 중 가장 많이 이동한 횟수 찾기
            Max = A[i].second - i;
        }
    }
    cout << Max + 1;

    return 0;
}