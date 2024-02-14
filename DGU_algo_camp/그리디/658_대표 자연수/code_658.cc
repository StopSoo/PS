// 배열의 가운데 위치에 있는 원소가 대표 자연수 !!
// 뭔가 이렇지 않을까? 의심되면 찔러보는 방법.
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	// 입력
	int N, number[20000];
	cin >> N;
	for (int i=0; i < N; i++) cin >> number[i];
	// 정렬
	sort(number, number+N);
	// 출력
	cout << number[(N-1)/2] << '\n';
	return 0;
}