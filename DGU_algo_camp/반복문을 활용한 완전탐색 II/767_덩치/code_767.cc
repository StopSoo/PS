#include <iostream>
using namespace std;

int main() {
	// 입력
	int N;
	cin >> N;
	int rank[N];	// 등수 배열
	int people[N][2];
	for (int i=0; i < N; i++)
		cin >> people[i][0] >> people[i][1];
	// 등수 계산(완전 탐색)
	for (int i=0; i < N; i++) {
		int bigger=0;	// 덩치가 큰 사람의 수
		for (int j=0; j < N; j++) {
			if (i == j) continue;
			if (people[i][0] < people[j][0] && people[i][1] < people[j][1]) bigger++;
		}
		rank[i] = bigger+1;
	}
	// 출력
	for (int i=0; i < N; i++)
		cout << rank[i] << " ";
	cout << '\n';
	return 0;
}