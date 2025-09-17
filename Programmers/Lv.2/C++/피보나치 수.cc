// https://school.programmers.co.kr/learn/courses/30/lessons/12945?language=cpp
// 시간 초과에 대한 해답은 메모이제이션 뿐인가 ...
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int memo[100001]= {};   // 0으로 초기화
int f(int n)
{
  if (memo[n] != 0) {
    return memo[n];
  }
  
  if (n==1 || n==2) {
    return memo[n] = 1;
  }
  else {
    return memo[n] = (f(n-1)+f(n-2))%1234567;
  }
}

int solution(int n) {
  int answer = 0;
  answer = (f(n-1) % 1234567 + f(n-2) % 1234567) % 1234567;
  return answer;
}

// 좀 더 나은 답안 (문제 옛날 ver.)
#include<iostream>
using namespace std;

long long fibonacci(int n)
{
  int i;
  long long dp[1000];
  dp[0]=0;
  dp[1]=1;

  for(i = 2; i <= n; i++) {
    dp[i]=dp[i-1]+dp[i-2];
  }

  return dp[n];
}