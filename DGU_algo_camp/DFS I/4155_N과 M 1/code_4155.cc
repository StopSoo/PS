// 재귀함수를 이용한 풀이
#include <iostream>
using namespace std;

int arr[10];
bool check[10] = {false, };	// 방문 여부 체크 배열
int N, M;

void dfs (int x) {	
	if (x == M + 1) {
		for (int i=1; i <= M; i++)
			cout << arr[i] << " ";
		cout << '\n';
		return;
	}
	for (int i=1; i <= N; i++) {
		if (check[i] == true) continue;
		arr[x] = i;
		check[i] = true;	// 방문 여부 체크
		dfs(x+1);
		check[i] = false;
	}
}

int main() {
	cin >> N >> M;
	
	dfs(1);
	
	return 0;
}