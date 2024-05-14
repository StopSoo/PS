// https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QPRjqA10DFAUq

#include<iostream>
#include <string>
using namespace std;

int main(int argc, char** argv)
{
	int number = 0;
    string str;
    cin >> str;
    
    for (int i=0; i < str.length(); i++) {
      number += str[i] - '0'; // 문자 -> 숫자 변환
    }
    
    cout << number << endl;
	return 0;
}