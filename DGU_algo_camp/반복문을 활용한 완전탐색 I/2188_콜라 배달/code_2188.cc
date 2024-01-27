// 1. 이중 반복문을 사용하는 방법
// 2. O(1) : N%5의 나머지 경우에 따라 조건문을 나누는 방법
// 3. O(n) : if ((N-i*3)%5 == 0) {j = (N-i*3)/5; ...}
#include <iostream>
using namespace std;

int main() {
	int N;
	cin >> N;
	
	int answer = -1;
	
	for (int i = 0; i * 3 <= N; i++) {
		for (int j = 0; j * 5 <= N; j++) {
			int total = i * 3 + j * 5;
			if (total == N) {
				int box = i + j;
				// 지금까지 구한 최소 상자 수보다 box 수가 작다면
				// or answer가 아직 갱신되지 않았다면
				if (answer == -1 || answer > box)
					answer = box;
			}
		}
	}
	
	cout << answer << '\n';
	return 0;
}