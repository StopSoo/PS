// https://school.programmers.co.kr/learn/courses/30/lessons/12921
// 아래 코드도 실행이 되나, "시간 초과" 때문에 해결하지 못 함.

#include <string>
#include <vector>

using namespace std;

bool isPrime(int num) {
  for (int i=2; i < num/2; i++)
    if (num % i == 0)
      return false;
  return true;
}

int solution(int n) {
  int answer = 0;
  for (int i=2; i < n; i++) {
    if (isPrime(i))
      answer++;
  }
  return answer;
}

// 에라토스테네스의 체를 사용한 효율적인 방식 (!)
#include <vector>
using namespace std;

int solution(int n) {
  vector<bool> isPrime(n + 1, true); // 모든 수를 소수로 초기화

  for (int i = 2; i * i <= n; i++) {  // 제곱근까지 반복문을 실행 (!)
    if (isPrime[i]) { // 소수인 경우
      for (int j = i * i; j <= n; j += i) {
        isPrime[j] = false; // 소수의 배수들은 소수가 아님
      }
    }
  }

  int answer = 0;
  for (int i = 2; i <= n; i++) {
    if (isPrime[i]) {
      answer++; // 소수인 경우 개수 증가
    }
  }
  return answer;
}
