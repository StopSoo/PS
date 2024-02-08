// 총 이동 횟수 = 2^n - 1
#include <iostream>
using namespace std;

void hanoi (int n, int s, int e) {
	if (n == 0) return;	// 원판의 개수가 0이 되었을 경우
	
	int o = 6 - s - e;	// 탑 1-3 중 s와 e가 아닌 나머지 하나를 o에 저장
	// 재귀함수 이용
	hanoi(n-1, s, o);	// n-1개의 원판을 s탑에서 o탑으로 이동시킴
	cout << s << " " << e << '\n';
	hanoi(n-1, o, e);	// n-1개의 원판을 o탑에서 e탑으로 이동시킴
}

int main () {
	int N;
	cin >> N;
	
	cout << (1 << N) - 1 << '\n';	// 옮긴 총 횟수
	hanoi(N, 1, 3);	// N개의 원판을 1번에서 3번으로 옮기는 과정
	
	return 0;
}