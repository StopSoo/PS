#include <iostream>
using namespace std;

int main() {
	// 입력
	int N, M, sum, count = 0;
	cin >> N >> M;
	
	int arr[N];
	for (int i = 0; i < N; i++)
		cin >> arr[i];
	
	for (int i = 0; i < N; i++) {
		sum = 0;
		for (int j = i; j <= N; j++) {
			sum += arr[j];
			if (sum == M) count++;
			if (sum > M) break;
		}
	}
	cout << count << endl;
	return 0;
}