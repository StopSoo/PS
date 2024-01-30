// Flood Fill을 이용 (!)
// 배열을 전체 탐색하면서 dfs에서 방문하지 않은 1이 있다면 해당 점을 기준으로 dfs를 하여 연결된 1들을 모두 검사한다.
// dfs에서는 연결된 1의 총 개수를 계수한다.
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int arr[25][25] = {0, };	// 값을 넣는 배열
int visited[25][25] = {0, };	// 방문 여부 체크 배열
int cnt=0, cnt_total=0;
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

void dfs(int x, int y) {
	// 해당 점에 대해서 dfs를 수행
	if (arr[x][y] == 0 || visited[x][y] == true) return;
	visited[x][y] = true;
	cnt++;
	
	for (int i=0; i < 4; i++) {
		// 상하좌우 좌표를 설정해서 dfs 돌리기
		int newx = x + dx[i];
		int newy = y + dy[i];
		if (newx >= 0 && newx < 25 && newy >= 0 && newy < 25) {
      dfs(newx, newy);
    }
	}
}

int main() {
	// 입력
	int N;
	vector<int> answer;
	cin >> N;
	for (int i=0; i < N; i++)
		for (int j=0; j < N; j++) {
			char c;
			cin >> c;
			arr[i][j] = c - '0';
		}
	// 체크
	for (int i=0; i < N; i++) {
		for (int j=0; j < N; j++) {
			if (arr[i][j] == 1 && visited[i][j] == false) {
				cnt = 0;
				dfs(i, j);
				cnt_total++;
				answer.push_back(cnt);
			}
		}
	}
	
	sort(answer.begin(), answer.end());	// 정렬
	
	cout << cnt_total << '\n';
	for (int i=0; i < answer.size(); i++)
		cout << answer[i] << '\n';
	return 0;
}