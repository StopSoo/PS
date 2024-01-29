// 재귀함수를 이용한 풀이
#include <iostream>
using namespace std;

int arr[10];
int check[10];
int N;

void dfs (int x) {
	if (x == N+1) {
		for (int i=1; i <= N; i++) 
			cout << arr[i] << " ";
		cout << '\n';
		return;
	}
	for (int i=1; i <= N; i++) {
		if (check[i] == true) continue;
		arr[x] = i;
		check[i] = true;	// 방문 여부 체크
		dfs(x+1);
		check[i] = false;	// 초기화
	}
}

int main() {
	cin >> N;
	
	dfs(1);
	
	return 0;
}