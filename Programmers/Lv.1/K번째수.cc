// https://school.programmers.co.kr/learn/courses/30/lessons/42748

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
  vector<int> answer;
  for (int i=0; i < commands.size(); i++) {
    vector<int> cut;
    for (int j=commands[i][0]-1; j < commands[i][1]; j++) // 인덱스임에 주의할 것.
      cut.push_back(array[j]);
    sort(cut.begin(), cut.end());   // 정렬
    answer.push_back(cut[commands[i][2]-1]);
  }
  return answer;
}