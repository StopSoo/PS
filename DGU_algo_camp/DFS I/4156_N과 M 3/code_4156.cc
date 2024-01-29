// 재귀함수를 이용한 풀이
#include <iostream>
using namespace std;

int arr[10];
int N, M;

void dfs (int x) {
	// M까지만 dfs를 돌고 M+1 때는 출력하고 끝내겠다는 의미
	if (x == M + 1) {
		for (int i=1; i <= M; i++) 
			cout << arr[i] << " ";
		cout << '\n';
		return;
	}
	for (int i=1; i <= N; i++) {
		arr[x] = i;
		dfs(x+1);
	}
}

int main() {
	cin >> N >> M;
	
	dfs(1);	// 1 -> 2 -> 3 -> ... 계속 진행
	
	return 0;
}