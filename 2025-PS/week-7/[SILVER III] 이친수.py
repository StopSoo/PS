# https://www.acmicpc.net/problem/2193

# 내 답안
# 각 자릿수 숫자마다 이친수의 개수 규칙을 찾아 DP 탐색 (!) -> 모르겠으면 처음엔 몇 개 찍어보기
# 첫 번째 답안 -> 답은 잘 나오나, 시간 초과! 절대 반복문으로 모든 수를 다 돌리면 안됨
# 두 번째 답안 -> DP(Dynamic Programming): memoization
N = int(input())
# count = 0
# for num in range(10**(N-1),10**N):
#   if (set(str(num)) == {'0', '1'} or set(str(num)) == {'1'}) and (not str(num).startswith('0')) and ('11' not in str(num)):
#     count += 1
# print(count)

dp = [0] * (N + 1)
dp[0] = 1 # 1자리 수에서 1개
dp[1] = 1 # 2자리 수에서 1개

for i in range(2, N+1):
  dp[i] = dp[i-1] + dp[i-2]
print(dp[N-1])