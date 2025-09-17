// https://school.programmers.co.kr/learn/courses/30/lessons/142086
// 97 = 'a'

#include <string>
#include <vector>

using namespace std;

vector<int> solution(string s) {
  vector<int> index(26, -1);
  vector<int> answer;
  for (int i=0; i < s.length(); i++) {
    if (index[s[i]-97] == -1) {   // 처음 나온 알파벳
      index[s[i]-97] = i; // 현재 인덱스를 저장
      answer.push_back(-1);
    } else {  // 처음 나오지 않은 알파벳
      answer.push_back(i - index[s[i]-97]);
      index[s[i]-97] = i;
    }  
  }
  return answer;
}