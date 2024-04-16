// https://school.programmers.co.kr/learn/courses/30/lessons/12943

#include <string>
#include <vector>

using namespace std;

int solution(int num) {
  int answer = 0;
  long long number = num;  // 자료형 주의 (!)
  
  if (number == 1) return 0;
  while (number != 1) {
    if (answer >= 500) {
      answer = -1;
      break;
    }
    answer++;
    
    number = (number % 2 == 0) ? number / 2 : number * 3 + 1;
  }
  return answer;
}
