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
	for (int i=0; i < n; i++) {
    for (int j=0; j < n-i-1; j++) {
      if (arr[j] > arr[j+1]) {
        int temp = arr[j];
        arr[j] = arr[j+1];
        arr[j+1] = temp;
        // 과정 출력
				for (int k=0; k < n; k++)
					cout << arr[k] << " ";
				cout << '\n';
      }
    }
  }
	
	return 0;
}