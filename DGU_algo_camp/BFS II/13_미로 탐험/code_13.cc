#include <iostream>
#include <queue>
using namespace std;

int dist[101][101] = {0, };	// 거리 배열
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

int main() {
	int N, M;
	cin >> N >> M;
	int arr[102][102] = {0, };	// 미로 -> 패딩 포함
	for (int i=1; i <= N; i++) {
		for (int j=1; j <= M; j++) {
			char c;
			cin >> c;
			arr[i][j] = c - '0';
		}
	}

	queue<int> q;
	q.push(1); q.push(1); q.push(1);
	while (!q.empty()) {
		int x = q.front(); q.pop();
		int y = q.front(); q.pop();
		int d = q.front(); q.pop();
		// 미로 칸이 벽이거나 한 번 방문한 곳은 체크하지 않음
		if (arr[x][y] == 0 || dist[x][y] > 0) continue;
		dist[x][y] = d;
		
		for (int i=0; i < 4; i++) {
			q.push(x + dx[i]);
			q.push(y + dy[i]);
			q.push(d+1);
		}
	}
	// 출력
	if (dist[N][M] == 0)
		cout << "-1" << '\n';
	else
		cout << dist[N][M] << '\n';
	return 0;
}