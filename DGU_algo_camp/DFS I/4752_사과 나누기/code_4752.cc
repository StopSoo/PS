#include <iostream>
using namespace std;

int p[20], arr[20];
int N;
long long mini = 9999999999;	// 주어진 범위에 따른 자료형에 유의할 것

void dfs (int x, long long diff) {	// diff = m - w
	// 남-여 차이를 인자로 넘겨 주는 방식
	if (x == N) {
		mini = min(mini, abs(diff));
		return;
	}
	dfs(x+1, diff + p[x]);	// 남자에게 주기
	dfs(x+1, diff - p[x]);	// 여자에게 주기
}

int main() {
	// 입력
	cin >> N;
	for (int i=0; i < N; i++)
		cin >> p[i];
	
	dfs(0, 0);
	// 출력
	cout << mini << '\n';
	return 0;
}