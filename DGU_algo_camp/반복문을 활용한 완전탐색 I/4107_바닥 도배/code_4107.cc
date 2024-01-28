#include <iostream>
#include <vector>
using namespace std;

int main() {
	int R, B, total, L, W;
	vector<int> divider;
	cin >> R >> B;
	total = R + B;
	// 약수 구하기 
	for (int i=2; i < total; i++) {
		if (total % i == 0)
			divider.push_back(i);
	}
	for (int i=0; i < divider.size(); i++) {
		int k = total / divider[i];
		if (divider[i]*2 + (k-2)*2 == R) {
			if (divider[i] > k) {
				L = divider[i];
				W = k;
			} else {
				L = k;
				W = divider[i];
			}
		}	
	}
	cout << L << " " << W << '\n';
	return 0;
}