// 반복자를 이용해서 set 원소들 출력하는 방법 익숙해지기
#include <iostream>
#include <set>
#include <string>
using namespace std;

int main() {
	// 입력 
	int N;
	set<string> people;
	set<string>::iterator iter;
	string name, log;
	cin >> N;
	for (int i=0; i < N; i++) {
		cin >> name >> log;
		if (log == "enter")
			people.insert(name);
		else
			people.erase(name);
	}
	
	cout << people.size() << '\n';
	for (iter=people.begin(); iter != people.end(); iter++) {
		cout << *iter << '\n';	
	}
	
	return 0;
}