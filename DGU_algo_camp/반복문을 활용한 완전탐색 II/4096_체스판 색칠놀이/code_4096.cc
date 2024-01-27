// 같은 색을 가진 두 좌표의 (x+y) 홀짝성이 같다. 
// 맨 왼쪽 위 칸이 B일 때 count 수와 W일 때 count 수의 합이 64인 것에 유의.
#include <iostream>
using namespace std;

int main() {
	// 입력
	int M, N, answer=64;
	int board[50][50];
	char c;
	cin >> M >> N;
	for (int i=0; i < M; i++) {
		for (int j=0; j < N; j++) {
			cin >> c;
			board[i][j] = (c == 'B');	// B인지 여부를 담기
		}
	}
	// 체크
	for (int r=0; r <= M-8; r++) {
		for (int l=0; l <= N-8; l++) {
			int count = 0;
			for (int w=r; w < r+8; w++) {
				for (int h=l; h < l+8; h++) {
					// 아래 코드는 모든 경우의 수가 압축된 코드.
					count += (board[w][h] == (w+h)%2);
				}
			}
			// answer의 값이 반복문을 거듭할수록 업데이트됨
      // 최소값을 두 번 체크한다는 점이 포인트(!)
			answer = min(answer, min(count, 64-count));
		}
	}
	
	cout << answer << '\n';
	return 0;
}