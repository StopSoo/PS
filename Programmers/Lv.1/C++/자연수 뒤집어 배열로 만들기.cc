// https://school.programmers.co.kr/learn/courses/30/lessons/12932?language=cpp

#include <string>
#include <vector>

using namespace std;

vector<int> solution(long long n) {
  vector<int> answer;
  string str = to_string(n);
  for (int i=str.length()-1; i >= 0; i--) {
    answer.push_back(str[i] - 48); // char와 int의 차이 -> 48 or '0'
  }
  return answer;
}

