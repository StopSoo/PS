// https://school.programmers.co.kr/learn/courses/30/lessons/12924
// 흐름을 잘 짜기 (!)

#include <string>
#include <vector>
using namespace std;

int solution(int n) {
  int answer = 0, tmp = 0;
  for (int i = 1; i <= n; i++) {
    tmp = i;
    for (int j = i + 1; j <= n; j++) {
      if (tmp == n) {
        answer++; 
        break;
      }
      if (tmp + j > n) break;

      tmp += j;
    }
  }
  return answer + 1;
}

// n의 약수 중 홀수 약수의 개수를 구해도 정답이 나옴 .. (왜?)
#include <string>
#include <vector>
using namespace std;

int solution(int n) {
  int answer = 0;
  int divider = 1;
  while (divider <= n) {
    // 홀수 약수를 구하는 조건
    if (0 == n % divider) answer++;
    divider += 2;
  }

  return answer;
}