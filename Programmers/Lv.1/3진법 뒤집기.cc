// https://school.programmers.co.kr/learn/courses/30/lessons/68935

#include <string>
#include <vector>

using namespace std;

int solution(int n) {
  int answer = 0;
  string number3 = ""; // 앞뒤 반전된 3진법 수 문자열
  int count = 0;
  while (n > 0) {
    number3 += to_string(n % 3);    // 숫자를 문자로 바꿔서 더해야 함(!)
    n = n / 3;
    count++;
  }    
  // 3진법 숫자를 앞뒤로 뒤집음 (!)
  int pow3 = 1;
  for (int i = count - 1; i >= 0; i--) {
    answer += (number3[i] - '0') * pow3;
    pow3 *= 3;
  }
  return answer;
}