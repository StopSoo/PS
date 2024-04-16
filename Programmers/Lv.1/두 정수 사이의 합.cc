// https://school.programmers.co.kr/learn/courses/30/lessons/12912

#include <string>
#include <vector>

using namespace std;

long long solution(int a, int b) {
  long long answer = 0;
  int max, min;
  if (a > b) {
    max = a; min = b;
  } else {
    max = b; min = a;
  }
  for (long long i = min; i <= max; i++)
    answer += i;
  return answer;
}

// 시그마 공식을 활용한 답안 => 1~n의 합은 n(n+1) / 2
#include <string>
#include <vector>

using namespace std;

long long solution(int a, int b) {
  return (long long)(a + b) * (abs(a - b) + 1) / 2;
}