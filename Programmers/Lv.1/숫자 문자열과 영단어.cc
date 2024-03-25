// https://school.programmers.co.kr/learn/courses/30/lessons/81301
// 문자열 일부 교체 : s.replace(s.find(바꿀 문자열), 바꿀 문자열의 길이, 바뀌는 문자열)

#include <string>
#include <vector>

using namespace std;

int solution(string s) {
  string word = s;
  vector<string> eng = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
  vector<string> num = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"};  // 좋은 말 할 때 문자열 말고 벡터로 쓰세요.
  
  for (int i=0; i < 10; i++) {
    int pos = word.find(eng[i]);   // 해당 문자열의 위치 찾기
    while (pos != string::npos) {   // 한 문자열이 더 이상 존재하지 않을 때까지 => 같은 문자열이 s에 여러 개 존재할 수 있으므로(!)
      word.replace(pos, eng[i].length(), num[i]); // 교체
      pos = word.find(eng[i], pos + 1); // 다음 위치부터 다시 찾기
    }
  }
  return stoi(word);
}

// 더 깔끔한 답안 ("regex_replace" 사용(!))
#include <bits/stdc++.h>
using namespace std;

int solution(string s) {
  s = regex_replace(s, regex("zero"), "0");
  s = regex_replace(s, regex("one"), "1");
  s = regex_replace(s, regex("two"), "2");
  s = regex_replace(s, regex("three"), "3");
  s = regex_replace(s, regex("four"), "4");
  s = regex_replace(s, regex("five"), "5");
  s = regex_replace(s, regex("six"), "6");
  s = regex_replace(s, regex("seven"), "7");
  s = regex_replace(s, regex("eight"), "8");
  s = regex_replace(s, regex("nine"), "9");    
  return stoi(s);
}