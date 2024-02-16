#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
	int N;
	cin >> N;
	map<string, int> books;
	map<string, int>::iterator it, mostFQ;
	string book;
	for (int i=0; i < N; i++) {
		cin >> book;
		if (books.find(book) != books.end())	// key가 이미 존재한다면
			books[book]++;
		else
			books[book] = 1;
	}
	// 체크
	mostFQ = books.begin();
	for (it=books.begin(); it != books.end(); it++) {
		if (it->second > mostFQ->second || (it->second == mostFQ->second && it->first < mostFQ->first)) {
			mostFQ = it;
		}
	}
	// 출력
	cout << mostFQ->first << '\n';
	return 0;
}