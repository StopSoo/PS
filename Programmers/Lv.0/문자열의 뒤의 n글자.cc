// https://school.programmers.co.kr/learn/courses/30/lessons/181910

#include <string>
#include <vector>

using namespace std;

string solution(string my_string, int n) {
  string answer = my_string.substr(my_string.size()-n);
  return answer;
}