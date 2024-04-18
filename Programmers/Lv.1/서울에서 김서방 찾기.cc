// https://school.programmers.co.kr/learn/courses/30/lessons/12919

#include <string>
#include <vector>

using namespace std;

string solution(vector<string> seoul) {
  int x;
  for (int i=0; i < seoul.size(); i++) {
    if (seoul[i] == "Kim") { 
      x = i;
      break;
    }
  }
  return "김서방은 " + to_string(x) + "에 있다";
}

// 또 다른 좋은 코드
#include <string>
#include <vector>
#include <iterator>
#include <algorithm>

using namespace std;

string solution(vector<string> seoul) {
  string answer = "";
  int pos = find(seoul.begin(),seoul.end(),"Kim")-seoul.begin();  // 체크 (!)
  answer = "김서방은 " + to_string(pos) + "에 있다";
  return answer;
}