// https://school.programmers.co.kr/learn/courses/30/lessons/12977?language=cpp

#include <vector>
#include <iostream>
using namespace std;

bool isPrime(int num) {
  for (int i=2; i < num; i++) {
    if (num % i == 0)
      return false;
  }
  return true;
}

int solution(vector<int> nums) {
  int answer = 0;
  // 완전 탐색 (N^3)
  for (int i=0; i < nums.size()-2; i++) {
    for (int j=i+1; j < nums.size()-1; j++) {
      for (int k=j+1; k < nums.size(); k++) {
        if (isPrime(nums[i] + nums[j] + nums[k]))
          answer++;
      }
    }
  }
  return answer;
}