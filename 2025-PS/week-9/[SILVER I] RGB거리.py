# https://www.acmicpc.net/problem/1149

# 내 답안
# 걸린 시간: 56ms
# 처음에는 규칙을 못 찾아서 한 25분 날린 듯?
# Bottom-Up 방식으로 푼 DP
# 하지만 다음부터 DP를 풀 때는 DP table을 만들면서 풀 것 !!
N = int(input())
money = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
  money[i][0] += min(money[i-1][1], money[i-1][2])
  money[i][1] += min(money[i-1][0], money[i-1][2])
  money[i][2] += min(money[i-1][0], money[i-1][1])

print(min(money[N-1]))