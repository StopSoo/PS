#include <iostream>
using namespace std;

char arr[100][100];
int visited[100][100] = {0, };    // 방문 여부 체크 배열
int count_p=0;    // 사람 -> 구역의 개수
int count_c=0;     // 소 -> 구역의 개수
int N;
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

void dfs_person(int x, int y, char color) {
  // 예외 상황을 먼저 정리하기
  if (x < 0 || x >= 100 || y < 0 || y >= 100) return;
	if (visited[x][y]) return;
	if (arr[x][y] != color) return;
    
  visited[x][y] = true;
  for (int i = 0; i < 4; i++) {
    int newx = x + dx[i];
    int newy = y + dy[i];
    if (newx >= 0 && newx < N && newy >= 0 && newy < N) { // N이 포인트 (!)
      dfs_person(newx, newy, color);
    }
  }
}

void dfs_cow(int x, int y, char color) {
  if (x < 0 || x >= 100 || y < 0 || y >= 100) return;
	if (visited[x][y]) return;
	// 적록색약 판별
	if (color == 'R' || color == 'G') {	
		if (arr[x][y] == 'B') return;
	} else {
		if (arr[x][y] == 'R' || arr[x][y] == 'G') return;
	}
	
  visited[x][y] = true;
	for (int i = 0; i < 4; i++) {
    int newx = x + dx[i];
    int newy = y + dy[i];
    if (newx >= 0 && newx < N && newy >= 0 && newy < N) {
      dfs_cow(newx, newy, color);
    }
  }
}

int main() {
  // 입력
  cin >> N;
  for (int i=0; i < N; i++) {
    for (int j=0; j < N; j++)
      cin >> arr[i][j];
  }
  // 사람 체크
  for (int i=0; i < N; i++) {
    for (int j=0; j < N; j++) {
      if (!visited[i][j]) {
        dfs_person(i, j, arr[i][j]);
          count_p++;
      }
    }
  }
  // 방문 여부 체크 배열 초기화
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      visited[i][j] = false;
    }
  }
  // 소 체크
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (!visited[i][j]) {
        dfs_cow(i, j, arr[i][j]);
        count_c++;
      }
    }
  }
  
  cout << count_p << " " << count_c << '\n';
  return 0;
}