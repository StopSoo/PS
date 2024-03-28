// https://school.programmers.co.kr/learn/courses/30/lessons/12926
// isupper() / islower() 함수 체크 (!)
// 나누기 연산 사용하는 것 체크 (!)

#include <string>
#include <vector>

using namespace std;

string solution(string s, int n) {
  string answer = "";
  for (int i=0; i < s.size(); i++) {
    if (s[i] == ' ')
      answer += ' ';
    else {
      char changed;
      if (isupper(s[i])) {    // 대문자라면
        changed = 'A' + (s[i] - 'A' + n) % 26;
      } else if (islower(s[i])) { // 소문자라면
        changed = 'a' + (s[i] - 'a' + n) % 26;
      }
      answer += changed;
      } 
    }
  return answer;
}