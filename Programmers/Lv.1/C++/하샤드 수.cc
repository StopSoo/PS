// https://school.programmers.co.kr/learn/courses/30/lessons/12947?language=cpp

#include <string>
#include <vector>

using namespace std;

bool solution(int x) {
  string str = to_string(x);
  int sum = 0;
  for (int i=0; i < str.length(); i++)
    sum += str[i] - '0';    // char to int 형 변환 까먹지 않기 (!)
  if (x % sum == 0) return true;
  else return false;
}