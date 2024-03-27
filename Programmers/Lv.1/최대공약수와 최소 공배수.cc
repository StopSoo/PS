// https://school.programmers.co.kr/learn/courses/30/lessons/12940

#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n, int m) {
  vector<int> answer;
  int gcd=0, lcm=0;
  // 최대공약수 찾기
  for (int i=1; i <= n; i++) {
    if (n % i == 0 && m % i == 0)
      gcd = i;
  }
  answer.push_back(gcd);
  // 최대공배수 찾기
  lcm = (n / gcd) * (m / gcd) * gcd;
  answer.push_back(lcm);
  return answer;
}