// https://school.programmers.co.kr/learn/courses/30/lessons/138477
/* 
  1. 최소값 찾기
  int minn = *min_element(answer.begin(), answer.end());
  2. 최소값이 위치한 인덱스 찾기
  int pos = find(answer.begin(), answer.end(), minn) - answer.begin();
  3. 해당 위치의 값을 제거하기
  answer.erase(answer.begin()+pos);
*/
// but, sort를 잘 이용하도록 하자 ! 
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(int k, vector<int> score) {
  vector<int> answer; // 제출할 답
  vector<int> awards; // 명예의 전당
  int min = 0;
  for (int i = 0; i < score.size(); i++) {
    if (awards.size() < k) {
      awards.push_back(score[i]);
      min = *min_element(awards.begin(), awards.end());   // 최소값 재설정
      answer.push_back(min);
    } else {
      int d = *min_element(awards.begin(), awards.end()); // 현재 명예의 전당에서의 최소값
      if (score[i] > d) {
        int pos = find(awards.begin(), awards.end(), d) - awards.begin();
        awards.erase(awards.begin() + pos);
        awards.push_back(score[i]);
      }
      min = *min_element(awards.begin(), awards.end()); // 최소값 재설정
      answer.push_back(min);
    } 
  }        
  return answer;
}