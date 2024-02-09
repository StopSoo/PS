// 굳이 memoization을 사용하지 않고도 ! 필요한 만큼만 문자열을 계산하면 됨.
// 보안 정책 위반 나오는데 해결 해야 함... 
#include <iostream>
#include <string>
using namespace std;

string makeStrings(int x) {
  if (x == 1) return "Hello ";
  if (x == 2) return "Hello Algo ";

  string prev = "Hello ";
  string curr = "Hello Algo ";

  for (int i = 3; i <= x; ++i) {
    string next = curr + prev;
    prev = curr;
    curr = next;
  }
  return curr;
}

int main() {
  int T;    // 테스트 케이스 수
  cin >> T;
  // 입력과 출력
  int number;
  for (int i = 0; i < T; i++) {
    cin >> number;
    string result = makeStrings(number);
    if (result.size() >= number && result[number - 1] == ' ') {
      cout << "Hello Algo" << endl;
    } else {
      cout << result[number - 1] << endl;
    }
  }

  return 0;
}
