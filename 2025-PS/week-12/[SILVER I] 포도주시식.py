# https://www.acmicpc.net/problem/2156

# 답안
# 걸린 시간: 292ms
# DP로 풀 생각을 해야 하는데, 이걸 DP로 어떻게 풀지 ,,? 이러고 있음 ㅋㅋㅋ
# DP 배열 = N잔의 포도주가 있을 때 최대로 마실 수 있는 양
# 경우의 수를 따질 때 모든 경우를 다 체크했는지 꼼꼼히 확인할 것 !! 
N = int(input())
drinks = [0] + list(int(input()) for _ in range(N))

dp = [0] * (N+1)
dp[1] = drinks[1]
if N >= 2: dp[2] = drinks[1] + drinks[2]
if N >= 3: dp[3] = max(drinks[1]+drinks[2], drinks[1]+drinks[3], drinks[2]+drinks[3])
if N >= 4:
  for i in range(4, N+1):
    dp[i] = max(dp[i-1], dp[i-2]+drinks[i], dp[i-3]+drinks[i-1]+drinks[i])
# 현재 안 마시고, 이전까지 누적 / 현재 잔을 마시고, 두 개 전 잔을 마신 경우 / 현재 잔과 직전 잔을 마신 경우 (!)
print(max(dp))