// https://school.programmers.co.kr/learn/courses/30/lessons/131705

#include <string>
#include <vector>

using namespace std;

int solution(vector<int> number) {
  int answer = 0;
  int num_p = number.size();  // 사람의 수
  // 조건에 맞게 완전 탐색 이용
  for (int i=0; i < num_p; i++) {
    for (int j=i+1; j < num_p; j++) {
      for (int k=j+1; k < num_p; k++) {
        if (number[i] + number[j] + number[k] == 0)
          answer++;
      }
    }
  }
  return answer;
}