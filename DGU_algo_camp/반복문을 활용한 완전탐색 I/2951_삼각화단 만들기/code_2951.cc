#include <iostream>
using namespace std;

int main() {
	int n, count=0;
	cin >> n;
	// 3중 반복문
	for (int i=1; i < n; i++) {
		for (int j=i; j < n; j++) {
			for (int k=j; k < n; k++) {
				if (i+j+k == n && i + j > k)
					count++;
			}
		}
	}
	// 2중 반복문
	for (int i=1; i <= n; i++) {
		for (int j=i; j < n; j++) {
			k = n-i-j;
			if (j <= k && i+j > k)
				count++;
		}
	}
	cout << count << '\n';
	return 0;
}