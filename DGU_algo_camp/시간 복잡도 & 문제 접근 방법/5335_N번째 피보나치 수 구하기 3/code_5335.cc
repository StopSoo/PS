#include <iostream>
#include <stdint.h>
using namespace std;

int main() {
	int N;
	cin >> N;
	uint64_t fibo[10001];
	fibo[1] = 1; fibo[2] = 2; fibo[3] = 4;

	for (int i=4; i <= N; i++)
		// 음수 값이 생기는 것을 방지하기 위해 미리 10억7을 더해줌 (!)
		fibo[i] = (fibo[i-1] + 2 * fibo[i-2] - fibo[i-3] + 1000000007) % 1000000007;
	// 출력
	cout << fibo[N] << '\n';
	return 0;
}