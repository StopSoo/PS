// https://school.programmers.co.kr/learn/courses/30/lessons/12911

#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int change(int n) { // 2진법으로 변환 후 1의 개수를 반환하는 함수
  int count=0;
  string result;
  int num = n;
  while (num != 1) {
    result += to_string(num % 2);
    num /= 2;
  }
  result += '1';
  reverse(result.begin(), result.end());
  
  for (int i=0; i < result.length(); i++)
    if (result[i] == '1') count++;
  
  return count;
}

int solution(int n) {
  int nextNumber = 0;
  int changedN = change(n);
  int i = n+1;
  while (1) {
    if (changedN == change(i)) {
      nextNumber = i;
      break;
    }
    else i++;
  }
  
  return nextNumber;
}

// bitset을 이용한 더 간단한 방법
// n이 100만까지이므로 20비트 이진수로 해결 가능 (!)
#include <bitset>

using namespace std;

int solution(int n) {
  int num = bitset<20>(n).count();  // 20비트 이진수로 변환 후 1의 개수를 셈

  while (bitset<20>(++n).count() != num);
  return n;
}