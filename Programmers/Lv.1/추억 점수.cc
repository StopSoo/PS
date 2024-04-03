// https://school.programmers.co.kr/learn/courses/30/lessons/176963

#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<string> name, vector<int> yearning, vector<vector<string>> photo) {
  vector<int> answer;
  
  for (int i=0; i < photo.size(); i++) {
    int score = 0;  // 사진마다의 추억 점수
    for (int j=0; j < photo[i].size(); j++) {
      for (int k=0; k < name.size(); k++) {
        if (photo[i][j] == name[k] && yearning.size() >= k+1) // 해당 사람의 추억 점수가 있을 경우에만 합
          score += yearning[k];
      }
    }
    answer.push_back(score);    
  }
  return answer;
}