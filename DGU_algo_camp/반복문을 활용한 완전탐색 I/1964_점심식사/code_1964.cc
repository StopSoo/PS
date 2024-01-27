#include <iostream>
using namespace std;

int main() {
	// 입력
	int N, C, food[1000], sum=0, count=0;
	cin >> N >> C;
	for (int i=0; i < N; i++)
		cin >> food[i];
	// 계산
	int max_count=0;
	for (int i=0; i < N; i++) {
		sum = 0;
		count = 0;
		for (int j=i; j < N; j++) {
			if (sum + food[j] <= C) {
				sum += food[j];
				count++;
				if (j == N-1) { // 끝에 도달할 경우
					if (count > max_count)
						max_count = count;
				}
			}	
			else {	// C를 초과했을 경우
				if (count > max_count)
					max_count = count;
				continue;
			}
		}
	}
	cout << max_count << '\n';
	return 0;
}