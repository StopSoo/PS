// https://school.programmers.co.kr/learn/courses/30/lessons/70129?language=cpp

#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string changeNumber(int num) { // 이진수로 변환하는 함수
  int number = num;
  string result = "";
  while (number != 1) {
    result += to_string(number % 2);
    number = number / 2;
  }
  result += '1';
  reverse(result.begin(), result.end());
  return result;
}

vector<int> solution(string s) {
  string str = s;
  int zeroCount=0, changeCount=0;
  vector<int> answer;
  while (str != "1") {
    changeCount++;
    int count=0;
    for (int i=0; i < str.length(); i++) {
      if (str[i] == '1') count++; // 1의 개수 체크
      else zeroCount++;
    }
    str = changeNumber(count);
  }
  answer.push_back(changeCount); answer.push_back(zeroCount);
  return answer;
}