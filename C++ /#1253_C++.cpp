// #1253 : 좋은 수
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);    // for fast i/o
    cin.tie(NULL);  // cin과 cout의 연결 해제
    cout.tie(NULL);

    int N;  // 배열 원소의 개수
    cin >> N;
    vector<int> A(N, 0);    // 원소의 개수 N, 0으로 초기화
    for (int i=0; i < N; i++)
        cin >> A[i];
    sort(A.begin(), A.end());   // 정렬

    int result = 0; // 좋은 수의 개수
    for (int k = 0; k < N; k++) {
        int find = A[k];    // 좋은 수인지 판별해야 하는 수
        int start = 0;  // 투 포인터 시작 인덱스
        int end = N-1;  // 투 포인터 끝 인덱스

        // 투 포인터 알고리즘
        while (start < end) {
            if (A[start] + A[end] == find) {
                if (start != k && end != k) {   // 두 수에 자신은 포함되면 안됨
                    result++;
                    break;
                } else if (start == k) start++;
                else if (end == k) end--;
            } else if (A[start] + A[end] > find)
                end--;
            else start++;   // A[start] + A[end] < find
        }
    }
    cout << result << endl;
}