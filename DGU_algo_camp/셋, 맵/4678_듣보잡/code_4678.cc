#include <iostream>
#include <string>
#include <set>
using namespace std;

int main() {
	// 입력
	int N, M, count=0;
	cin >> N >> M;
	set<string> nListen;
	string person;
	for (int i=0; i < N; i++) {
		cin >> person;
		nListen.insert(person);
	}
	for (int i=0; i < M; i++) {
		cin >> person;
		// find() : 해당 원소가 배열에 없을 경우 end()를 반환함.
		if (nListen.find(person) != nListen.end())
			count++;
	}
	
	cout << count << '\n';
	return 0;
}