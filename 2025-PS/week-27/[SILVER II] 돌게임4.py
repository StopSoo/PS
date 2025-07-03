# https://www.acmicpc.net/problem/9658

# 내 답안
# 걸린 시간: 40ms
# 규칙을 빨리 찾는 게 중요 (!) 여기서는 7개마다 반복된다. (7개는 직접 구해보기)
N = int(input())
dp = [0] * (N + 1) # 0은 상근 패, 1은 상근 승
for i in range(2, N + 1):
  dp[i] = 0 if (i % 7 == 1 or i % 7 == 3) else 1
print("SK" if dp[N] == 1 else "CY")