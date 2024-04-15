// https://school.programmers.co.kr/learn/courses/30/lessons/181933

#include <string>
#include <vector>

using namespace std;

int solution(int a, int b, bool flag) {
  if (flag == true)
    return a + b;
  else
    return a - b;
}