// https://school.programmers.co.kr/learn/courses/30/lessons/42862
// 정답율 93.3%까지 가고 포기 ...
// 깔끔한 모범 답안 익히기 (!)

#include <string>
#include <vector>
using namespace std;

int student[35];  // 전역 변수로 선언 시 0으로 초기화

int solution(int n, vector<int> lost, vector<int> reserve) {
  int answer = 0;
  for (int i : reserve) student[i] += 1;
  for (int i : lost) student[i] += -1;

  for (int i = 1; i <= n; i++) {
    if (student[i] == -1) { // 도난 당한 경우
      if (student[i-1] == 1) // 내 앞 사람이 체육복을 가지고 있거나 
        student[i-1] = student[i] = 0;
      else if (student[i+1] == 1) // 내 뒷 사람이 체육복을 가지고 있거나 
        student[i] = student[i+1] = 0;
    }
  }
  // 최종 개수 카운트 
  for(int i  = 1; i <= n; i++)
    if(student[i] != -1) answer++;

  return answer;
}

// 원래 내가 작성한 답안 -> 너무 복잡함
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
  int answer = n;
  
  for (int i=0; i < lost.size(); i++) {
    // 체육복을 가져온 학생이 체육복을 도난 당했을 때
    if (find(reserve.begin(), reserve.end(), lost[i]) != reserve.end()) {
      reserve.erase(remove(reserve.begin(), reserve.end(), lost[i]), reserve.end());
      continue;
    }
        
    if (find(reserve.begin(), reserve.end(), lost[i]-1) != reserve.end()) {
      reserve.erase(remove(reserve.begin(), reserve.end(), lost[i]-1), reserve.end());
    } else if (find(reserve.begin(), reserve.end(), lost[i]+1) != reserve.end()) {
      reserve.erase(remove(reserve.begin(), reserve.end(), lost[i]+1), reserve.end());
    } else {
      answer--;
    }       
  }
  
  return answer;
}