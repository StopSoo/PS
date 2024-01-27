// 다시 확인하기
// #include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
	// 입력
	int N, answer=0;
	string target, str;
	
	cin >> N;
	cin >> target;	// 새로운 표지
	
	while (N--) {
		cin >> str;
		
		bool pos = false;
		for (int s=0; s < str.size(); s++) {	// 기존 표지 문자열 돌기
			for (int d=1; d < str.size(); d++) {	// 간격 
				if (s + d*(target.size()-1) >= str.size()) continue;
				
				bool flag = true;
				for (int k=0; k < target.size(); k++) {
					if (target[k] != str[s+k*d]) flag = false;
				}
				if (flag) pos = true;
			}
		}
		if (pos) answer++;
	}
	cout << answer << '\n';	
	return 0;
}