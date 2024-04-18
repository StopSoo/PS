// https://school.programmers.co.kr/learn/courses/30/lessons/12944?language=cpp

#include <string>
#include <vector>
#include <numeric>  // accumulate를 위한 헤더 파일

using namespace std;

double solution(vector<int> arr) {
  // accumulate의 세 번째 인자를 초기값
  double answer = (double)accumulate(arr.begin(), arr.end(), 0) / arr.size();
  return answer;
}