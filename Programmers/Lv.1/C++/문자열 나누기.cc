// https://school.programmers.co.kr/learn/courses/30/lessons/140108?language=cpp
// 로직 짜기의 중요성 (!)

#include <string>
#include <vector>

using namespace std;

int solution(string s) {
  int answer = 0;
  string str = s;
  int length = str.length(), start = 0;
  
  while (start < length) {
    char x = str[start];
    int c_x=0, c_notX=0;
    int i = start;
    
    while (i < length) {
      if (str[i] == x) c_x++;
      else c_notX++;
      
      if (c_x == c_notX) {
        answer++;
        start = i + 1;
        break;
      }
      i++;
    }
    if (i == length) {  // c_x와 c_notX의 개수가 같지 않을 경우
      answer++;
      break;
    }
  }
  
  return answer;
}
