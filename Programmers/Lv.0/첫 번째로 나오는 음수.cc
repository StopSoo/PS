// https://school.programmers.co.kr/learn/courses/30/lessons/181896

#include <string>
#include <vector>

using namespace std;

int solution(vector<int> num_list) {
  for (int i=0; i < num_list.size(); i++) {
    if (num_list[i] < 0) {
      return i;
      break;
    }
  }
  return -1;
}