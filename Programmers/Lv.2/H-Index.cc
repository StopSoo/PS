// https://school.programmers.co.kr/learn/courses/30/lessons/42747
// 맞추긴 했으나 번잡하다 ... 

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> citations) {
  int answer = 0;
  vector<int> c = citations;  // 매개변수로 받은 벡터도 바로 정렬 가능하다고 함.
  sort(c.begin(), c.end()); // 정렬
  
  for (int i=0; i <= 10000; i++) {
    int count = 0;
    for (int j=0; j <= c.size(); j++) {
      if (c[j] >= i) {
        count = c.size() - j;
        break;
      }
    }
    if (count == 0) break;  // 위 반복문 내 조건에 한 번도 해당되지 않은 경우
    if (count >= i) 
      answer = i;
  }
  
  return answer;
}

// 본래 작성하고자 했던 의도의 코드
// 반복문 안에 조건식을 간결하게 작성하는 것이 중요할 것 같다 (!)
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> citations) {
  int answer = 0;

  sort(citations.begin(), citations.end());
  for (int i = 0; i < citations.size(); i++) {
    if (citations.size() - i <= citations[i]) {
      answer = citations.size() - i;
      break;
    }
  }

  return answer;
}

