#include <iostream>
using namespace std;

int main() {
	// 입력
	int N, M, W, H, sum=0, max=0;
	cin >> N >> M;	// 연못 NXM
	cin >> W >> H;	// 그물 WXH
	
	int area[100][100];
	for (int i=0; i < N; i++)
		for (int j=0; j < M; j++)
			cin >> area[i][j];
	
	// 탐색
	for (int i=0; i <= N-W; i++) {
		for (int j=0; j <= M-H; j++) {
			sum = 0;
			for (int k=0; k < W; k++) {
				for (int l=0; l < H; l++) {
					sum += area[i+k][j+l];
				}
			}
			if (max < sum) max = sum;
		}
	}
  // 출력
	cout << max << '\n';
	return 0;
}