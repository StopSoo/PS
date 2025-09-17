// https://school.programmers.co.kr/learn/courses/30/lessons/12906
/* 헷갈리는 점 확실히 짚기 (!)
  vector v에 대해
  - v.erase(v.begin()+s, v.begin()+e) : [s, e) 구간의 원소들 삭제.
  - unique(v.begin(), v.end()) : 중복된 원소들을 제거하고, 원래 벡터 배열의 나머지 자리엔 기존 벡터 배열의 원소가 채워짐.
  => v.erase(unique(v.begin(), v.end()), v.end()) : 중복 없이 필요한 원소만 뽑아낼 수 있음 !!
*/
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr) 
{
  vector<int> answer = arr;
  answer.erase(unique(answer.begin(), answer.end()), answer.end());
  return answer;
}