#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main() {
	string command;
	int number;
	stack<int> stack;
	
	for (int i=0; i < 100000; i++) {
		// 공백이 오기 전 문자열까지만 입력됨 
		cin >> command;
		
		if (command == "push") {
      // 이렇게 숫자를 따로 입력 받아도 상관 X
			cin >> number;
			stack.push(number);
			cout << stack.top() << '\n';
		} else if (command == "pop") {
			if (stack.empty())
				cout << "-1" << '\n';
			else {
				cout << stack.top() << '\n';
				stack.pop();
			}
		} else if (command == "size") {
			cout << stack.size() << '\n';
		} else if (command == "empty") {
			if (stack.empty())
				cout << "1" << '\n';
			else
				cout << "0" << '\n';
		} else if (command == "top") {
			if (stack.empty())
				cout << "-1" << '\n';
			else
				cout << stack.top() << '\n';
		} else if (command == "end") {
			break;
		}
	}
	
	return 0;
}