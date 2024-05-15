// https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&problemLevel=2&contestProbId=AV5QFuZ6As0DFAUq&categoryId=AV5QFuZ6As0DFAUq&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=CCPP&select-1=2&pageSize=10&pageIndex=1

#include <iostream>
using namespace std;

int main(int argc, char** agrv) {
  for (int i=0; i < 5; i++) {
    for (int j=0; j < 5; j++) {
      if (i == j) cout << "#";
      else cout << "+";
    }
    cout << endl;
  }
  cout << endl;
  
  return 0;
}