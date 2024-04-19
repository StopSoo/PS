// https://school.programmers.co.kr/learn/courses/30/lessons/159994
// 아무래도 테스트케이스에 문제가 있는 듯 ..

#include <string>
#include <vector>

using namespace std;


string solution(vector<string> cards1, vector<string> cards2, vector<string> goal) {
  int l = 0;
  int r = 0;

  for (string& g: goal) {
    if (g == cards1[l]) l++;
    else if (g == cards2[r]) r++;
    else return "No";
  }

  return "Yes";
}