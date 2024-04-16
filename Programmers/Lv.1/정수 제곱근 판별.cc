// https://school.programmers.co.kr/learn/courses/30/lessons/12934?language=cpp
// 자료형에 유의 (!) => 오래 걸린 이유는 제어 변수 자료형을 int로 했기 때문 ...

#include <string>
#include <vector>
#include <cmath>

using namespace std;

long long solution(long long n) {
  long long answer = -1;
  for (long long i=1; i <= sqrt(n); i++) {  
    if (i * i == n) {
      answer = (i+1)*(i+1);
      break;
    }
  }
  return answer;
}
