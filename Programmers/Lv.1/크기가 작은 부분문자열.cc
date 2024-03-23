//  https://school.programmers.co.kr/learn/courses/30/lessons/147355?language=cpp

#include <string>
#include <vector>

using namespace std;

int compareStrings(string str1, string str2) {
  // 예외 처리
  if (str1.size() != str2.size())
    return str1.size() - str2.size();
  // 두 문자열의 값이 같을 경우는 0을, str1이 더 작으면 음수를, str1이 더 크면 양수를 반환
  return str1.compare(str2);
}

int solution(string t, string p) {
  int answer = 0;
  int tLen = t.length();
  int pLen = p.length();
  
  for (int i = 0; i <= tLen - pLen; i++) {
    string subStr = t.substr(i, pLen);  // 부분 문자열
    if (compareStrings(subStr, p) <= 0) // str1의 값이 작거나 같을 경우
      answer++;
  }
  return answer;
}
