# https://www.acmicpc.net/problem/14501

# 내 답안
# 걸린 시간: 52ms
# DP 문제인데 조건부 DFS로 풀었음. 조건을 설정하는 게 살짝 까다로웠음!
def find_max_profit(day, now_profit):
  global T, P
  
  ok_choose, not_choose = now_profit, now_profit
  if day <= N and day+(T[day]-1) <= N:
    ok_choose = find_max_profit(day+T[day], now_profit+P[day])
  if day+1 <= N:
    not_choose = find_max_profit(day+1, now_profit)
  
  return max(ok_choose, not_choose)

N = int(input())
T, P = [0], [0] # 시간, 이익 (인덱스1부터 시작)
for _ in range(N):
  t, p = map(int, input().split())
  T.append(t)
  P.append(p)

print(find_max_profit(1, 0))

# DP 답안
# 걸린 시간: 36ms
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [0 for _ in range(N)]
for i in range(N):
  duration, profit = arr[i] # 시간, 이익
  end_day = i + duration - 1 # 오늘 시작한 작업이 끝나는 날
  
  if end_day < N:
    # i일에 시작해서 end_day에 끝나는 작업
    dp[end_day] = max(dp[end_day], (dp[i-1] if i>0 else 0) + profit)
  # 이전 날짜까지의 최대값 이어가기
  dp[i] = max(dp[i], dp[i-1] if i > 0 else 0)

print(dp[-1])