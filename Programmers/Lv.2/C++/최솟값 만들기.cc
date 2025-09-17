// https://school.programmers.co.kr/learn/courses/30/lessons/12941

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> A, vector<int> B)
{
  int answer = 0;
  vector<int> X = A;
  vector<int> Y = B;
  sort(X.begin(), X.end());
  sort(Y.rbegin(), Y.rend());
  // 서로 반대 방향으로 정렬 후 곱한 게 최솟값 !
  for (int i=0; i < X.size(); i++) {
    answer += X[i] * Y[i];
  }

  return answer;
}