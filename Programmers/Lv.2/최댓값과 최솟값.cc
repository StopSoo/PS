// https://school.programmers.co.kr/learn/courses/30/lessons/12939
// 결국엔 stringstream ... (!)

#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

string solution(string s) {
  stringstream ss(s);
  vector<int> numbers;
  int num;

  // 문자열 ss에서 숫자를 읽어 numbers 벡터에 저장
  while (ss >> num) {
    numbers.push_back(num);
    // 스트림의 공백을 건너뜀
    if (ss.peek() == ' ')
      ss.ignore();
  }

  int maxNum = *max_element(numbers.begin(), numbers.end());
  int minNum = *min_element(numbers.begin(), numbers.end());

  return to_string(minNum) + " " + to_string(maxNum);
}

// 기존 코드
// substr() 함수와 vector 사용이 비효율적임 => 시간 초과 뜸

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string s) {
  string answer = "";
  string str = s;
  string str1, str2;
  vector<int> numbers;
  
  while (str.length() != 0) {
    str1 = str.substr(0, str.find(' '));
    numbers.push_back(stoi(str1));
    if (str.length() == 1 || str.length() == 2) break;
    else str = str.substr(str.find(' ') + 1);
  }

  int max = *max_element(numbers.begin(), numbers.end());
  int min = *min_element(numbers.begin(), numbers.end());
  answer = to_string(min) + " " + to_string(max);
  return answer;
}
