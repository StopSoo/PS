// https://school.programmers.co.kr/learn/courses/30/lessons/12917

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string s) {
  string answer = "";
  vector<char> original;
  for (int i=0; i < s.length(); i++)
    original.push_back(s[i]);
  sort(original.rbegin(), original.rend());   // 내림차순 정렬 
  for (int i=0; i < original.size(); i++)
    answer += original[i];
  return answer;
}

// 더 간단하고 깔끔한 방법
// string도 vector다 (!)
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string solution(string s) {
  sort(s.rbegin(),s.rend());
  return s;
}