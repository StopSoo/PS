# https://www.acmicpc.net/problem/11051

# 이 문제의 의도: 조합 공식을 이용해서 memoization을 구현하는 것 (!)
# 답안 1
# 걸린 시간: 44ms
N, K = map(int, input().split())
up, down = 1, 1
for i in range(K): # (N-K)! 계산의 간소화
  up = up * N
  down = down * K
  N -= 1
  K -= 1
print((up // down) % 10007)

# 답안 2
# 걸린 시간: 40ms
N, K = map(int, input().split())

dp = [1] * (N + 1) # 팩토리얼 값을 저장 
for i in range(2, N+1): dp[i] = dp[i-1] * i

if K == 0 or K == N: print(1) # nCn = 1
elif K == 1: print(N % 10007)
else: print((dp[N] // (dp[K] * dp[N-K])) % 10007) 