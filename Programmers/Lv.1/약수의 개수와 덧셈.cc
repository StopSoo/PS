// https://school.programmers.co.kr/learn/courses/30/lessons/77884

#include <string>
#include <vector>

using namespace std;

// 약수의 개수가 짝수인지를 리턴하는 함수
bool check(int number) {
  int answer = 0;
  for (int i = 1; i <= number; i++) {
    if (number % i == 0)
      answer++;
  }
  return answer % 2 == 0;
}

int solution(int left, int right) {
  int answer = 0;
  for (int i = left; i <= right; i++) {
    if (check(i))
      answer += i;
    else
      answer -= i;
  }
  return answer;
}