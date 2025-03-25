# https://www.acmicpc.net/problem/2749

# 답안
# 걸린 시간: 592ms
# 피보나치 수를 K로 나눈 나머지는 항상 주기를 가지게 되는데, 이는 피사노 주기(Pisano Period)라고 한다.
# M = 10^k일 때 k > 2라면, 주기는 항상 15*10^(k-1)이다.
mod = 1000000 # 나누는 수
p = mod//10 * 15 # 나머지 주기 

fibo = [0] * p
fibo[1] = 1
for i in range(2, p):
  fibo[i] = fibo[i-1] + fibo[i-2]
  fibo[i] %= mod

n = int(input())
print(fibo[n%p])