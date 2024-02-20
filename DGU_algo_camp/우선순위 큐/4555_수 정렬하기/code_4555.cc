// merge sort 
#include <iostream>
using namespace std;

int temp[1000000];

void merge_sort(int *arr, int s, int e) {
	// s부터 e-1까지 정렬하는 코드 (!)
	if (e-s == 1) return;
	
	int mid = (s+e) / 2;
	merge_sort(arr, s, mid);	// s부터 mid-1까지
	merge_sort(arr, mid, e);	// mid부터 e-1까지
	
	int lp=s, rp=mid;
	for (int i=s; i < e; i++) { 
		// 값 비교 뿐만이 아니라, 배열 범위를 벗어났는지도 체크해줘야 함 !!
		// rp == e : 오른쪽 배열 원소를 모두 사용했는지
		// lp < mid : 왼쪽 배열 원소가 남아 있는지
		if (rp == e || (lp < mid && arr[lp] < arr[rp]))
			temp[i] = arr[lp++];
		else
			temp[i] = arr[rp++];
	}
	for (int i=s; i < e; i++)
		arr[i] = temp[i];
}

int main() {
	// 입력
	int N;
	int arr[1000000];
	cin >> N;
	for (int i=0; i < N; i++)
		cin >> arr[i];
	
	merge_sort(arr, 0, N);
	// 출력
	for (int i=0; i < N; i++)
		cout << arr[i] << '\n';
	return 0;
}