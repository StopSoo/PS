#include <iostream>
using namespace std;

int main() {
	// 입력
	int n;
	cin >> n;
	int arr[100];
	for (int i=0; i < n; i++)
		cin >> arr[i];
	// 처음 상태 출력
	for (int i=0; i < n; i++)
		cout << arr[i] << " ";
	cout << '\n';
	// 버블 정렬
	int count = n;
	while (count >= 1) {
		for (int i=0; i < n-1; i++) {
			if (arr[i] > arr[i+1]) {
				int temp = arr[i];
				arr[i] = arr[i+1];
				arr[i+1] = temp;
				// 과정 출력
				for (int j=0; j < n; j++)
					cout << arr[j] << " ";
				cout << '\n';
			}
		}
		count--;
	}
	
	return 0;
}