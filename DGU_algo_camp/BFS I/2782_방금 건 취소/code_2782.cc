#include <iostream>
#include <stack>
using namespace std;

int main() {
	int K, number, sum=0;
	stack<int> stack;
	cin >> K;
	
	for (int i=0; i < K; i++) {
		cin >> number;
		if (number == 0) {
			sum -= stack.top();
			stack.pop();
		}
		else {
			stack.push(number);
			sum += number;
		}
	}
	
	cout << sum << '\n';
	return 0;
}