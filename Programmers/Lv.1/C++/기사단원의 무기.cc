// https://school.programmers.co.kr/learn/courses/30/lessons/136798?language=cpp
// 본래 작성했던 코드는 시간 초과 문제로 통과하지 못함.
// 계산 최소화를 위한 벡터 배열 사용.

#include <string>
#include <vector>
#include <cmath>

using namespace std;

vector<int> calculateDivisorCounts(int maxNumber) {
  vector<int> divisorCounts(maxNumber + 1, 0);
  
  for (int i = 1; i <= maxNumber; i++) {
    for (int j = i; j <= maxNumber; j += i) {
      divisorCounts[j]++;
    }
  }
  
  return divisorCounts;
}

int solution(int number, int limit, int power) {
  vector<int> divisorCounts = calculateDivisorCounts(number);
  int answer = 0;
  
  for (int i = 1; i <= number; i++) {
    int divisorsCount = divisorCounts[i];
    
    if (divisorsCount <= limit) {
      answer += divisorsCount;
    } else {
      answer += power;
    }
  }
  
  return answer;
}
