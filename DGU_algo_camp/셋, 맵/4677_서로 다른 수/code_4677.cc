// set은 자동 정렬이 됨 (!)
#include <iostream>
#include <set>
using namespace std;

int main() {
	int N, num;
	cin >> N;
	set<int> s;
	for (int i=0; i < N; i++) {
		cin >> num;
		s.insert(num);
	}
	
	cout << s.size() << '\n';
	return 0;
}