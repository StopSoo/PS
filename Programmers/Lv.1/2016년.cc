// https://school.programmers.co.kr/learn/courses/30/lessons/12901?language=cpp

#include <string>
#include <vector>

using namespace std;

vector<int> months = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}; // 윤년을 고려한 월별 날짜 수
vector<string> day = {"FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"};  // 시작은 1월 1일의 요일로 설정.
string solution(int a, int b) {
  string answer = "";
  // 총 날짜 수 계산
  int days = -1;
  for (int i=0; i < a-1; i++)
    days += months[i];
  days += b;
  
  answer = day[days % 7];
  return answer;
}