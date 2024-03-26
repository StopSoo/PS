// https://school.programmers.co.kr/learn/courses/30/lessons/12935

// 모범 답안 (min_element 이용하기(!))
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> solution(vector<int> arr) {
  vector<int> answer = arr;

  int nMin = *min_element(arr.begin(), arr.end());
  int pos = find(answer.begin(), answer.end(), nMin) - answer.begin();
  answer.erase(answer.begin() + pos);

  return answer.empty() ? vector<int>(1, -1) : answer;
}