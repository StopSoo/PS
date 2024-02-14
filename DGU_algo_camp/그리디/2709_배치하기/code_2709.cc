#include <iostream>
#include <algorithm>
using namespace std;

bool desc(int a, int b){ 
  return a > b; 
}

int main() {
	// 입력
	int N;
	long long result=0;	// long long에 주의 !!!
	cin >> N;
	int A[50], B[50];
	for (int i=0; i < N; i++) cin >> A[i];
	for (int i=0; i < N; i++) cin >> B[i];
	// 정렬
	sort(A, A+N);
	sort(B, B+N, desc);
	// 계산 및 출력
	for (int i=0; i < N; i++) result += A[i]*(long)B[i];
	cout << result << '\n';
	return 0;
}