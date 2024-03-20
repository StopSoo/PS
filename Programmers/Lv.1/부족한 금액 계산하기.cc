// https://school.programmers.co.kr/learn/courses/30/lessons/82612#

#include <iostream>

long long solution(int price, int money, int count) {
  long long all_price = 0;
  for (int i = 1; i <= count; i++){
    all_price += price * i;
  }
  if (all_price > money) {
    return all_price - money;
  }
  else {
    return 0;
  }
}