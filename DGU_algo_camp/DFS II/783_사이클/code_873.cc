#include <iostream>
#include <vector>
using namespace std;

vector<int> visited(1001, 0);	// 방문 여부 체크 배열 
int ans, N, P;

int dfs (int x, int round) {
	if (visited[x] == 0) {
		visited[x] = round;
		dfs((x*N)%P, round+1);
	} else
		ans = round - visited[x];
}

int main () {
	cin >> N >> P;
	
	dfs(N, 1);
	
	cout << ans << '\n';
	return 0;
}