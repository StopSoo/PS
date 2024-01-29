#include <iostream>
using namespace std;

int main() {
	// 입력
	int N, count=0;
	double sum=0.0, avg=0.0;
	int arr[1000];
	cin >> N;
	for (int i=0; i < N; i++)
		cin >> arr[i];
	// 체크
	for (int s=0; s < N; s++) {
		sum = 0.0;
		for (int e=s; e < N; e++) {
			sum += arr[e];
			avg = sum / (e-s+1);
			for (int i=s; i <= e; i++) {
				if (avg == arr[i]) {
					count++;
					break;
				}
			}
		}
	}
	// 출력
	cout << count << '\n';
	return 0;
}