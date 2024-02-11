#include<iostream>
#include<algorithm>
using namespace std;

int A[1000001];
int upper_bound(int N, int *arr, int K){
	int index = N;
	int s=0, e=N-1, mid;	// 시작, 종료, 가운데 인덱스
	
	while (s <= e) {
		mid = (s+e) / 2;
		if (A[mid] <= K) {
			s = mid+1;
		} else {
			index = mid;
			e = mid-1;
		}
	}
	return index+1;
}

int main()
{
	// 입력
	int n, k;
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> A[i];
	cin >> k;
	// 출력
	cout << upper_bound(n, A, k) << '\n';
	return 0;
}