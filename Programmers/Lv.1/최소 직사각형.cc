// https://school.programmers.co.kr/learn/courses/30/lessons/86491?language=cpp

#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> sizes) {
  int answer = 0;
  int max_width = 0, max_height = 0;

  for (int i = 0; i < sizes.size(); ++i) {
    // 명함을 가로로 놓았을 때의 최대 길이(최대들 중의 최대)
    max_width = max(max_width, max(sizes[i][0], sizes[i][1]));
    // 명함을 세로로 놓았을 때의 최대 길이(최소들 중의 최대)
    max_height = max(max_height, min(sizes[i][0], sizes[i][1])); 
  }
  
  answer = max_width * max_height;
  return answer;
}