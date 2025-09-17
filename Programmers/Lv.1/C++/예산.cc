// https://school.programmers.co.kr/learn/courses/30/lessons/12982

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> d, int budget) {
  sort(d.begin(), d.end()); // 오름차순 정렬 (!)
  
  int count = 0;
  int remainingBudget = budget;
  
  for (int amount : d) {
    if (remainingBudget >= amount) {
      remainingBudget -= amount;
      count++;
    } else {
      break; 
    }
  }
  return count;
}