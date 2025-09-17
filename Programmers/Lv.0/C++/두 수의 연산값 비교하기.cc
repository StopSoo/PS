// https://school.programmers.co.kr/learn/courses/30/lessons/181938

#include <string>
#include <vector>

using namespace std;

int solution(int a, int b) {
  int answer = stoi(to_string(a) + to_string(b));
  return answer >= 2 * a * b ? answer : 2 * a * b;
}