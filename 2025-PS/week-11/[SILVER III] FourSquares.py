# https://www.acmicpc.net/problem/17626

# 내 답안
# 걸린 시간: 120ms (pypy3)
# 시간 초과 해결 방법
# 1) 50001까지 돌리던 걸 n까지만 돌리도록 수정.
# 2) O(N)의 시간 복잡도를 가지는 min 함수를 사용할 때는 잘 따져보고 사용하기.
# 3) 굳이 필요하지 않다면 리스트에 추가하는 로직을 없앨 것.
import math

def make_dp(n):
  dp = [0] * (n+1)
  square_number = [] # 현재 수로부터 가장 가까운 제곱수

  for i in range(1, n+1):
    if int(math.sqrt(i))**2 == i: # 제곱수인 경우
      dp[i] = 1
      square_number.append(i)
    else:
      min_value = float('inf')
      for s_num in square_number: # 어떤 제곱수가 최적의 제곱수일지 모르므로 다 돌려보기 (!)
        if i - s_num < 0: break
        min_value = min(min_value, 1 + dp[i - s_num])
      dp[i] = min_value
  return dp

n = int(input())
dp = make_dp(n)
print(dp[n])