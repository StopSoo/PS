// 1. dp를 정의한다. -> dp[n] = 2Xn 크기의 ~~~ 경우의 수.
// 2. 관계식을 정의한다. -> dp[n] = dp[n-1] + dp[n-2] (상황을 적용해보면 알 수 있음.)
#include <iostream>
#define number 10007
using namespace std;

int main() {
	int n;
	cin >> n;
	
	int *dp = new int[1001];
	dp[1] = 1; dp[2] = 2;	// 초기값 설정
	for (int i=3; i <= n; i++) {
		dp[i] = (dp[i-1] + dp[i-2]) % number;
	}
	
	cout << dp[n] << '\n';
	delete [] dp;
	return 0;
}
