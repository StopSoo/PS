// https://school.programmers.co.kr/learn/courses/30/lessons/86051?language=cpp

#include <string>
#include <vector>

using namespace std;

int solution(vector<int> numbers) {
  int answer = 0;
  vector<bool> isExist(10, false);  // 숫자의 등장 여부 저장 배열

  for (int i=0; i < numbers.size(); i++) {
    isExist[numbers[i]] = true;
  }

  for (int i=0; i < 10; i++) {
    if (!isExist[i])
      answer += i;
  }

  return answer;
}

// * 비둘기집의 원리를 이용한 효율적인 모범 답안

// #include <string>
// #include <vector>

// using namespace std;

// int solution(vector<int> numbers) {

//     int answer = 45;

//     for (int i = 0 ; i < numbers.size() ; i++)
//         answer -= numbers[i];

//     return answer;
// }