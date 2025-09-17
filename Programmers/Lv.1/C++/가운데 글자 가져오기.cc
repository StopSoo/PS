// https://school.programmers.co.kr/learn/courses/30/lessons/12903
// 앞으로는 substr()을 활용한 방법도 생각해보기 (!)

#include <string>
#include <vector>

using namespace std;

string solution(string s) {
  string answer = "";
  int len_s = s.length();
  if (len_s % 2 == 0) {
    answer += s[len_s/2 - 1];
    answer += s[len_s/2];
  }
  else
    answer = s[len_s/2];
  return answer;
}