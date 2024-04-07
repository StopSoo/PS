// https://school.programmers.co.kr/learn/courses/30/lessons/135808

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int k, int m, vector<int> score) {
  int answer = 0;
  int n = score.size(); // 주어진 사과의 개수
  int maxBoxes = n / m;   // 상자의 최대 개수 계산
  vector<int> sorted_score = score;
  sort(sorted_score.rbegin(), sorted_score.rend());
  
  for (int i = 0; i < maxBoxes; i++) {
    int minE = *min_element(sorted_score.begin() + i*m, sorted_score.begin() + (i + 1)*m);
    answer += minE * m;
  }
  return answer;
}