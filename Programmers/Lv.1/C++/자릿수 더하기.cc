// https://school.programmers.co.kr/learn/courses/30/lessons/12931

#include <iostream>
#include <string>

using namespace std;
int solution(int n)
{
  int answer = 0;
  string n_str = to_string(n);
  for (int i=0; i < n_str.length(); i++) {
    answer += n_str[i] - '0'; // 문자를 숫자로 바꿀 때 헷갈리지 않기 (!)
  }
  return answer;
}