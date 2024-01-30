// DFS를 이용한 Flood Fill : 바깥에 물 붓기
// 0이면서 물이 차 있는 것만 둘레로 체크.
// 바깥을 1칸 정도 패딩시키기
// 건초더미의 상하좌우의 “외부 빈칸”의 개수의 총합
#include <iostream>
using namespace std;

int arr[102][102] = {0, };	// 값을 저장할 배열 (패딩 포함)
int visited[102][102] = {false, };	// 방문 여부 체크 배열 (패딩 포함)
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};
int answer = 0;	// 둘레

void dfs (int x, int y) {
	visited[x][y] = true;
	for (int i=0; i < 4; i++) {
		int newx = x + dx[i];
		int newy = y + dy[i];
    // 배열 범위 체크
		if (newx < 0 || newx > 101 || newy < 0 || newy > 101)
			continue;
		if (arr[newx][newy] == 0 && visited[newx][newy] == false)
			dfs(newx, newy);
	}
}

int main() {
	// 입력
	int N;
	cin >> N;
	for (int i=0; i < N; i++) {
		int x, y;
		cin >> x >> y;
		arr[x][y] = 1;
	}

	dfs(0, 0);  // (0,0)부터 dfs를 수행
	
	for (int i=1; i <= 100; i++) {
		for (int j=1; j <= 100; j++) {
			if (arr[i][j] == 1) {
				for (int k=0; k < 4; k++) {
					// 해당 점의 상하좌우에 대해 dfs를 적용
					int newi = i + dx[k];
					int newj = j + dy[k];
					if (arr[newi][newj] == 0 && visited[newi][newj] == true)
						answer++;
				}
				
			}
		}
	}
	
	cout << answer << '\n';
	return 0;
}