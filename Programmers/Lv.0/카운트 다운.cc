// https://school.programmers.co.kr/learn/courses/30/lessons/181899

#include <string>
#include <vector>

using namespace std;

vector<int> solution(int start, int end_num) {
  vector<int> answer;
  for (int i=start; i >= end_num; i--) {
    answer.push_back(i);
  }
  return answer;
}