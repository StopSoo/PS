#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
  int N, M;
  cin >> N >> M;
  vector<vector<char>> room(N, vector<char>(M));	// 방의 값
  vector<vector<bool>> visited(N, vector<bool>(M, false)); // 방문 여부
  // 입력
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      cin >> room[i][j];
    }
  }
  // 방향 설정
  int dx[] = {-1, 1, 0, 0};
  int dy[] = {0, 0, -1, 1};
  // BFS 
  auto bfs = [&](int x, int y) {
    queue<pair<int, int>> q;
    q.push({x, y});	
    visited[x][y] = true;	// 방문 여부 체크

    while (!q.empty()) {
      int cx = q.front().first;
      int cy = q.front().second;
      q.pop();

      for (int i = 0; i < 4; i++) {
  // 상하좌우 체크
        int nx = cx + dx[i];
        int ny = cy + dy[i];

        if (nx >= 0 && nx < N && ny >= 0 && ny < M) {
          // 빈 공간이면서 아직 방문하지 않았다면
          if (room[nx][ny] == '.' && !visited[nx][ny]) {
            q.push({nx, ny});
            visited[nx][ny] = true;
          }
        }
      }
    }
  };

  int roomCount = 0;	// 방 개수
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      if (room[i][j] == '.' && !visited[i][j]) {
        bfs(i, j);
        roomCount++;
      }
    }
  }
  // 출력
  cout << roomCount << endl;

  return 0;
}
