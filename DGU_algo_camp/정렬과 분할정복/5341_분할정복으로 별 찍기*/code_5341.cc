// 프랙탈을 출력하라는 문제.
// 재귀 함수 이용.
#include <iostream>
#include <vector>
using namespace std;

void frac (vector<vector<char>>& arr, int n, int x, int y) {
	// 배열을 1 or 0으로 채우기
	if (n == 1)  {
		arr[x][y] = '*';
		return;
	}
	for (int i=0; i < 3; i++) {
		for (int j=0; j < 3; j++) {
			if (i == 1 && j == 1) 
				continue;
			frac(arr, n/3, x + n/3*i, y + n/3*j);
		}
	}
}

int main() {
	// 입력
	int N;
	cin >> N;
	vector<vector<char>> arr(N, vector<char>(N, ' '));
	
	frac(arr, N, 0, 0);
	
	// 출력
	for (int i=0; i < N; i++) {
		for (int j=0; j < N; j++) {
			cout << arr[i][j];
		}
		cout << '\n';
	}
  
	return 0;
}