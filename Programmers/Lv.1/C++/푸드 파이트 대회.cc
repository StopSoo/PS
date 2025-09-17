// https://school.programmers.co.kr/learn/courses/30/lessons/134240?language=cpp

#include <string>
#include <vector>
#include <algorithm>  // for reverse

using namespace std;

string solution(vector<int> food) {
  string answer = ""; // 제출할 답
  string temp = ""; // 임시로 저장할 문자열
  for (int i=1; i < food.size(); i++) {
    int count = food[i] / 2;
    while (count--) {
      temp += to_string(i);
    }
  }
  answer += temp;

  answer += '0';  // 물 저장
  // 문자열을 뒤집어서 답 문자열에 더하기
  // reverse해서 바로 다른 문자열에 저장 불가능(!)
  reverse(temp.begin(), temp.end());  
  answer += temp;
  return answer;
}

// 더 간단하고 깔쌈한 코드
#include <string>
#include <vector>

using namespace std;

string solution(vector<int> food) {
  string answer = "0";
  int check;
  for(int i=food.size()-1; i>0; i--){
    check = food[i]/2;
    while(check){    
      answer = to_string(i) + answer + to_string(i);
      check--;
    }
  }
  return answer;
}