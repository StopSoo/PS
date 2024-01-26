// 변수 초기화에 유의할 것
#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
	// 입력
    int N;    // 점의 개수
	int points[5000][5000];    // 점의 좌표, 색깔
    int result = 0;
    cin >> N;
    for (int i=0; i < N; i++) {
        for (int j=0; j < 2; j++)
            cin >> points[i][j];
    }
    // 계산
    for (int i=0; i < N; i++) {
        int minLen = 100000;
        for (int j=0; j < N; j++) {
            if (i == j) continue;
            if (points[i][1] == points[j][1] && abs(points[i][0] - points[j][0]) < minLen) {
                minLen = abs(points[i][0] - points[j][0]);
            }
        }
        result += minLen;
    }
    cout << result << '\n';
    return 0;
}