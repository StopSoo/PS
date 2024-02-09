// 삽입 정렬 : 두 번째 자료부터 시작하여 그 앞쪽의 자료들과 비교하여 삽입할 위치를 지정한 후, 지정한 자리에 자료를 삽입
#include <iostream>
using namespace std;

int main() {
	// 입력
	int n, count=0;
	cin >> n;
	int arr[100];
	for (int i=0; i < n; i++)
		cin >> arr[i];
	// 처음 상태 출력
	for (int i=0; i < n; i++)
		cout << arr[i] << " ";
	cout << '\n';
	// 삽입 정렬
	for (int i=0; i < n; i++) {
		for (int j=i; j > 0; j--) {
			if (arr[j] < arr[j-1]) {
				int temp = arr[j];
				arr[j] = arr[j-1];
				arr[j-1] = temp;
				// 과정 출력
				for (int k=0; k < n; k++)
					cout << arr[k] << " ";
				cout << '\n';
			}
		}
	}

	return 0;
}