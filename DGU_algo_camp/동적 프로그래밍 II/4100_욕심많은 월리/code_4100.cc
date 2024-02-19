// dp(x, i) : (1~i)번 물건만 사용하여 무게 x로 고를 수 있는 물건의 최대 가치 합
#include <iostream>
#include <cmath>
using namespace std;

int main() {
	// 입력
	int N, W;
	cin >> N >> W;
	long long dp[101][100000] = {0, };
	
	for (int i=1; i <= N; i++) {
		int x, v;	// 무게, 가치 
		cin >> x >> v;	
		for (int j=1; j <= W; j++) {
			// i번째 것을 안 고르는 경우와 고르는 경우
			dp[i][j] = dp[i-1][j];
			if (j-x >= 0)
				dp[i][j] = max(dp[i][j], dp[i-1][j-x] + v);
		}
	}
	// 출력
	cout << dp[N][W] << '\n';	
	return 0;
}