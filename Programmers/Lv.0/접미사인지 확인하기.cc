// https://school.programmers.co.kr/learn/courses/30/lessons/181908

#include <string>
#include <vector>

using namespace std;

int solution(string my_string, string is_suffix) {
  if (is_suffix.size() > my_string.size()) return 0;
  
  if (my_string.substr(my_string.size()-is_suffix.size(), is_suffix.size()) == is_suffix) 
    return 1;
  else return 0;
}