// https://school.programmers.co.kr/learn/courses/30/lessons/131701

#include <string>
#include <vector>
#include <set>
using namespace std;

int solution(vector<int> elements) {
  set<int> sums;
  for (int i=0; i < elements.size(); i++) {   // 합의 시작점 인덱스
    int sum=0;
    for (int j=0; j < elements.size(); j++) {  // 합할 원소의 개수
      if (i+j >= elements.size()) // 원형 수열을 고려
        sum += elements[i+j-elements.size()];
      else
        sum += elements[i+j];
      sums.insert(sum);
    }
  }
  return sums.size();
}

// 좀 더 정돈된 코드
#include <string>
#include <vector>
#include <set>

using namespace std;

int solution(vector<int> elements) {
  set<int> S;

  int n = elements.size();

  for (int i = 0 ; i < n ; ++i) {
    int sum = 0;
    for (int j = i ; j < i + n ; ++j) {
      sum += elements[j % n]; // (!)
      S.insert(sum);
    }
  }

  return S.size();
}