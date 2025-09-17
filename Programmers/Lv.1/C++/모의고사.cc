// https://school.programmers.co.kr/learn/courses/30/lessons/42840
// vector 내 최대값/최소값 구하기 => max_element/min_element 포인터로 사용.
// 아래 코드는 내가 처음 작성한 코드 + 보완

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
  vector<int> p1 = {1, 2, 3, 4, 5};
  vector<int> p2 = {2, 1, 2, 3, 2, 4, 2, 5};
  vector<int> p3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

  vector<int> answer, counts(3);  // 제출할 배열과 문제 정답 수가 들어있는 배열 -> 배열 크기를 정하면자동으로 0으로 초기화(!)
  for (int i=0; i < answers.size(); i++) {
    if (answers[i] == p1[i % p1.size()]) counts[0]++;
    if (answers[i] == p2[i % p2.size()]) counts[1]++;
    if (answers[i] == p3[i % p3.size()]) counts[2]++;
  }  
  // 가장 많은 문제를 맞힌 사람 체크
  int max_value = *max_element(counts.begin(), counts.end());   // 최대값 구하는 부분 한 줄로 해결(!)
  for (int i=0; i < 3; i++) {
    if (counts[i] == max_value) answer.push_back(i+1);
  }
  return answer;
}
