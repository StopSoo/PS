#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	// 입력
	int n, j=0, A[100000], B[100000], count=0;
	cin >> n;
	for (int i=0; i < n; i++) cin >> B[i];
	for (int i=0; i < n; i++) cin >> A[i];
	// 정렬
	sort(A, A+n);
	sort(B, B+n);
	// 계산
	for (int i=0; i < n; i++) {
		while (j < n && A[j] <= B[i]) j++;
		if (j == n) break;
		count++;
		j++;
	}
	// 출력
	cout << count << '\n';
	return 0;
}