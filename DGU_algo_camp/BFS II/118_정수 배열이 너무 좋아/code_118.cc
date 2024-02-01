// n 값이 크기 때문에, 시간 복잡도를 최소화하는 방향으로 가야 함 -> 덱을 뒤집는 함수 구현 X
#include <iostream>
#include <deque>
#include <string>
using namespace std;

int main() {
	// 입력
	int n;
	deque<int> dq;
	string key;
	bool isFront = true;	// 배열의 앞뒤 여부 (!)
	cin >> n;
	for (int i=0; i < n; i++) {
		int num;
		cin >> num;
		dq.push_back(num);
	}
	cin >> key;
	// 체크 
	for (int i=0; i < key.length(); i++) {
		// 키에 따른 처리
		if (key[i] == 'X') {	// X
			// 배열이 비어 있는지를 확인
			if (dq.empty()) {
				cout << "Error" << '\n';
				return 0;
			}
			// 변수 값에 따라 배열 원소를 앞에서 빼거나, 뒤에서 빼거나 (!)
			if (isFront) {
				dq.pop_front();
			} else {
				dq.pop_back();
			}
		} else {	// R
			// 실제 함수를 만드는 게 아니라, 순서를 뒤집은 것처럼 보이게 할 것 (!)
			isFront = !isFront;
		}
	}
	// 배열이 비어 있는지를 확인하고 아니라면 출력
	if (dq.empty()) {
		cout << "Error" << '\n';
		return 0;
	} else {
		if (isFront) {
			for (int i=0; i < dq.size(); i++)
				cout << dq[i] << " ";
			cout << '\n';
		} else {
			for (int i=dq.size()-1; i >= 0; i--)
				cout << dq[i] << " ";
			cout << '\n';
		}
	}

	return 0;
}