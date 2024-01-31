// C++은 pop해서 바로 값을 변수에 저장할 수 없음 !! 
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
	// 입력
	int N, M;
	queue<int> q;
	vector<int> person;	// 조세퍼스 순열
	cin >> N >> M;
	for (int i=1; i <= N; i++)	// 사람 번호를 큐에 삽입
		q.push(i);
	
	while (!q.empty()) {
		for (int i=1; i < M; i++) {
			// M-1개는 큐의 맨 뒤로 보내고 (!)
			int x = q.front();
			q.pop();
			q.push(x);
		}
		// M번째는 출력한다. (!)
		int x = q.front();
		q.pop();
		person.push_back(x);
	}
	// 출력
	for (int i=0; i < N; i++)
		cout << person[i] << " ";
	cout << '\n';
	return 0;
}