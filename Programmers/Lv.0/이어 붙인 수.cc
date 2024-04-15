// https://school.programmers.co.kr/learn/courses/30/lessons/181928

#include <string>
#include <vector>

using namespace std;

int solution(vector<int> num_list) {
  string hol = "", jjak = "";
  for (int i=0; i < num_list.size(); i++) {
    if (num_list[i] % 2 == 1)
      hol += to_string(num_list[i]);
    else
      jjak += to_string(num_list[i]);
  }
  return stoi(hol) + stoi(jjak);
}