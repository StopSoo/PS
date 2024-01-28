#include <iostream>
using namespace std;

int main() {
	int N;
	cin >> N;
	long long fibo[10000];
	fibo[1] = 1; fibo[2] = 1;
	// 계산 과정마다 나누기 연산을 해줄 것.
	for (int i=3; i <= N; i++)
		fibo[i] = (fibo[i-1] + fibo[i-2]) % 1000000007;
	cout << fibo[N] << '\n';
	
	return 0;
}