// https://school.programmers.co.kr/learn/courses/30/lessons/181906

#include <string>
#include <vector>

using namespace std;

int solution(string my_string, string is_prefix) {
  int answer = 0;
  string str = "";
  for (int i=0; i < my_string.size(); i++) {
    str += my_string[i];
    if (is_prefix == str) {
      answer = 1;
      break;
    }
  }
  return answer;
}

// 훨씬 더 짧고 간결한 답안 => substr() 사용하기 (!)
#include <string>
#include <vector>

using namespace std;

int solution(string my_string, string is_prefix) {    
  return my_string.substr(0, is_prefix.size()) == is_prefix;
}