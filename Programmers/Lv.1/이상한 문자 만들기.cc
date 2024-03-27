// https://school.programmers.co.kr/learn/courses/30/lessons/12930

// 근데 내가 짠 코드 너무 하드코딩 ...
// 공백인지 확인하는 함수 -> isspace()
// 혹은 " "가 아닌, ' '로 체크할 것.
// 제어 변수가 잘 증가/감소하고 있는지 체크할 것.

#include <string>
#include <vector>

using namespace std;

string solution(string s) {
  string answer = "";
  int len_s = s.length(); // 문자열의 전체 길이
  int index = 0;  // 단어별 인덱스
  for (int i=0; i < len_s; i++) {
    if (isspace(s[i])) {   // 공백일 경우
      index = 0;
      answer += " ";
      continue;
    }
    
    if (index % 2 == 0) {
      if (s[i] >= 97)
        answer += s[i] - 32;
      else
        answer += s[i];
    }
    else if (index % 2 == 1) {
      if (s[i] < 97)
        answer += s[i] + 32;
      else
        answer += s[i];
    }
    index++; 
  }
  return answer;
}

// 좀 더 깔끔한 코드
// toupper(), tolower() 함수를 적극 활용할 것 (!)
#include <string>
#include <vector>

using namespace std;

string solution(string s) {
  string answer = "";
  int nIndex = 1;
  for (int i = 0; i < s.size(); i++, nIndex++) {
    if (s[i] == ' ') {  // 공백인지 확인
      nIndex = 0;
      answer += " ";
    }
    else
      nIndex & 1 ? answer += toupper(s[i]) : answer += tolower(s[i]);
  }
  return answer;
}