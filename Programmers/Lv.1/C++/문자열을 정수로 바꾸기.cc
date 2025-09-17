// https://school.programmers.co.kr/learn/courses/30/lessons/12925
// 포인트 : stoi 함수는 문자열 내 부호까지 그대로 바꿔준다. 

#include <string>
#include <vector>

using namespace std;

int solution(string s) {
  int answer = stoi(s);
  return answer;
}