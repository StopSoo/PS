// https://school.programmers.co.kr/learn/courses/30/lessons/12933
// 내 코드 .. so 복잡 ..

#include <string>
#include <vector>
#include <algorithm>
using namespace std;

long long solution(long long n) {
  long long x = 0;
  string answer = to_string(n);
  vector<char> number;
  for (int i=0; i < answer.length(); i++)
    number.push_back(answer[i]);
  
  sort(number.begin(), number.end());   // 정렬
  
  int count=1;
  for (int i=0; i < number.size(); i++) {
    x += count * (number[i] - '0'); // 일의 자리부터 계산해서 더함
    count *= 10;  // 자릿수 계산
  }
  return x;
}

// 깔끔하고 좋은 코드
// 문자열도 정렬이 된다는 것 (!) 잊지 않기
// stoi 개념으로 stoll 함수의 존재 파악 (!)
#include <string>
#include <vector>
#include <algorithm>
#include <functional> // greater 사용을 위함
using namespace std;

long long solution(long long n) {
  long long answer = 0;

  string str = to_string(n);
  sort(str.begin(), str.end(), greater<char>());  // greater<char> : 내림차순 정렬
  answer = stoll(str);

  return answer;
}