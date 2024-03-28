// https://school.programmers.co.kr/learn/courses/30/lessons/12918?language=cpp

// 처음 작성한 답안
#include <string>
#include <vector>
#include <iostream>

using namespace std;

bool solution(string s) {
  bool answer = true;
  if (s.length() != 4 && s.length() != 6) {   // 문자열의 길이 조건
    answer = false;
    return answer;
  }
  for (int i=0; i < s.length(); i++) {    // 문자열의 알파벳 조건
    if (s[i] - '0' > 9) {
      answer = false;
      return answer;
    }
  }
  return answer;
}

// 더 간소화시킨 답안
// isdigit() : 한 문자가 int인지 검사, 예를 들어 a는 char이므로 false 반환

#include <string>
#include <vector>
#include <iostream>

using namespace std;

bool solution(string s) {
  bool answer = true;
  for (int i=0; i < s.length(); i++) {
    if (!isdigit(s[i])) {   
      answer = false;
      return answer;
    }
  }
  return (s.length() == 4 || s.length() == 6) ? answer : false;
}