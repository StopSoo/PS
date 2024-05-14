// https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5Pl0Q6ANQDFAUq&categoryId=AV5Pl0Q6ANQDFAUq&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=CCPP&select-1=2&pageSize=10&pageIndex=1
// 1. 변수 선언 시 자료형 주의 -> 범위에 맞는 자료형 사용할 것
// 2. 배열 초기값 주의

#include <iostream>
#include <vector>
using namespace std;

int main() {
  long long T, num;
  cin >> T;

  long long arr[T][5] = {{0, }};

  for (int i = 0; i < T; i++) {
    cin >> num;
    while (num != 1) {
      if (num % 2 == 0) {
        arr[i][0]++;
        num /= 2;
      } else if (num % 3 == 0) {
        arr[i][1]++;
        num /= 3;
      } else if (num % 5 == 0) {
        arr[i][2]++;
        num /= 5;
      } else if (num % 7 == 0) {
        arr[i][3]++;
        num /= 7;
      } else if (num % 11 == 0) {
        arr[i][4]++;
        num /= 11;
      }
    }
    // 출력
    cout << "#" << i+1 << " " << arr[i][0] << " " << arr[i][1] << " ";
    cout << arr[i][2] << " " << arr[i][3] << " " << arr[i][4] << endl;
  }

  return 0;
}