// https://school.programmers.co.kr/learn/courses/30/lessons/132267
// 내가 놓친 포인트는 크게 float / 반복문 내 복잡한 로직

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int a, int b, int n) {
  int answer = 0;
  int bottle = n;

  while ((float)bottle/a >= 1) {
    answer += bottle / a * b;
    bottle = bottle / a * b + bottle % a;
  }

  return answer;
}
