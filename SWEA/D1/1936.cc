// https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5PjKXKALcDFAUq&categoryId=AV5PjKXKALcDFAUq&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=CCPP&select-1=1&pageSize=10&pageIndex=1
// 조건식이 헷갈리면, 경우의 수가 적으니까 그냥 단순 조건문으로 작성해도 될 듯 !

#include<iostream>
using namespace std;

int main(int argc, char** argv) {
  int num_a, num_b;
  cin >> num_a >> num_b;

  if (num_a == (num_b + 1) % 3)
    cout << "B" << endl;
  else
    cout << "A" << endl;

  return 0;
}