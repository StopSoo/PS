// 재귀함수를 이용한 풀이
// N과 M 3 문제와 거의 같지만, 시작 지점을 정한다는 것이 다르다!! -> 매개변수 int s
#include <iostream>
using namespace std;

int arr[10];
int N, M;

void dfs (int x, int s) {	
	if (x == M + 1) {
		for (int i=1; i <= M; i++)
			cout << arr[i] << " ";
		cout << '\n';
		return;
	}
	for (int i=s; i <= N; i++) {
		arr[x] = i;
		dfs(x+1, i+1);
	}
}

int main() {
	cin >> N >> M;
	
	dfs(1, 1);
	
	return 0;
}