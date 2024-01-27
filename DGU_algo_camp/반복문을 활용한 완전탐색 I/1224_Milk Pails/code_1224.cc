#include <iostream>
using namespace std;

int main() {
	int X, Y, M, total=0;
	cin >> X >> Y >> M;
	// 완전탐색
	for (int i=0; i*X <= M; i++) {
		for (int j=0; j*Y <= M; j++) {
			int sum = i*X + j*Y;
			if (sum > total && sum <= M)
				total = sum;
		}
	}
	cout << total << '\n';
	return 0;
}