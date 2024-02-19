#include <iostream>
#include <cmath>
using namespace std;

int main() {
	// 입력
	int N, maxi=0;
	int arr[1000], LIS[1001]={0, };
	cin >> N;
	for (int i=0; i < N; i++)  {
		cin >> arr[i];
		for (int j=0; j < i; j++)
			if (arr[j] < arr[i])
				LIS[i] = max(LIS[i], LIS[j]);
		LIS[i]++;
		
		maxi = max(maxi, LIS[i]);
	}
	
	cout << maxi << '\n';
	return 0;
}