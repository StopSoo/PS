// https://school.programmers.co.kr/learn/courses/30/lessons/181929

#include <string>
#include <vector>

using namespace std;

int solution(vector<int> num_list) {
  int sum=0, mul=1;
  for (int i=0; i < num_list.size(); i++) {
    sum += num_list[i];
    mul *= num_list[i];
  }

  if (mul < sum * sum) return 1;
  else return 0;
}

// 더 간단한 코드 -> accumulate() 사용 (!)
// int sum = accumulate(v.begin(), v.end(), 0); -> 세 번째 인자는 초기값
// int product = accumulate(v.begin(), v.end(), 1, multiplies<int>());
#include <bits/stdc++.h>
#define all(x) (x).begin(), (x).end()
using namespace std;

int solution(vector<int> num_list) {
  return accumulate(all(num_list), 1, multiplies<int>()) < pow(accumulate(all(num_list), 0), 2) ? 1 : 0;
}