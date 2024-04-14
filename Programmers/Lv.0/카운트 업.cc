// https://school.programmers.co.kr/learn/courses/30/lessons/181920

#include <string>
#include <vector>

using namespace std;

vector<int> solution(int start_num, int end_num) {
  vector<int> answer;
  for (int i=start_num; i <= end_num; i++)
    answer.push_back(i);
  return answer;
}