// https://school.programmers.co.kr/learn/courses/30/lessons/12909

#include<string>
#include <iostream>

using namespace std;

bool solution(string s)
{
  bool answer = true;
  // 괄호 별 개수 체크
  int left=0, right=0;
  for (int i=0; i < s.length(); i++) {
    if (s[i] == '(') left++;
    else {
      right++;
      if (left < right) return false;
    }
  }
  // 예외 케이스 체크
  if (left != right) answer = false;
  else if (s[s.length()-1] == '(') answer = false;
  else if (s[0] == ')') answer = false;
  return answer;
}

// 간결하고 좋은 코드
#include<string>
#include <iostream>

using namespace std;

bool solution(string s)
{
  int n = 0;
  for (int i = 0; i < s.length(); i++) {
    if (n < 0)  // (보다 )가 먼저 나왔다는 뜻
      return false;
    if (s[i] == '(')
      n++;
    else if (s[i] == ')')
      n--;
  }
  return n == 0;
}