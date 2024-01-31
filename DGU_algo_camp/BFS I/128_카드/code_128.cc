#include <iostream>
#include <queue>
using namespace std;

int main() {
	int N;
	queue<int> q;
	cin >> N;
	for (int i=1; i <= N; i++)
		q.push(i);
	// 체크
	while (q.size() > 1) {
		q.pop();
		q.push(q.front());
		q.pop();
	}
	// 출력
	cout << q.front() << '\n';
	return 0;
}