#include <iostream>
using namespace std;

int main() {
	// 재귀 함수 말고 memoization으로 풀기 !!
	int N;
	cin >> N;
	long fibo[505];
	fibo[1] = 1; fibo[2] = 1;
	for (int i=3; i <= N; i++)
		fibo[i] = fibo[i-1] + fibo[i-2];
	
	cout << fibo[N] << '\n';
	
	return 0;
}