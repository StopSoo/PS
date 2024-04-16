// https://school.programmers.co.kr/learn/courses/30/lessons/12916

#include <string>
#include <iostream>
using namespace std;

bool solution(string s)
{
  int num_p=0, num_y=0;
  for (int i=0; i < s.length(); i++) {
    if (s[i] == 'p' || s[i] == 'P') num_p++;
    if (s[i] == 'y' || s[i] == 'Y') num_y++;
  }
  if (num_p == num_y) return true;
  else return false;
}