# https://www.acmicpc.net/problem/9657

# 답안
# 걸린 시간: 40ms
# "두 사람이 완벽하게 게임을 했다" -> 자신이 이기는 쪽으로 조정해서 게임했다.
# 사실 아래 코드는 잘 이해가 안됨
N = int(input())
if (N%7 == 1) or (N%7 == 3) or (N%7 == 4) or (N%7 == 5) or (N%7 == 6): print("SK")
else: print("CY")

# 내가 이해할 수 있는 코드
# 걸린 시간: 44ms
# dp[i-1], dp[i-3], dp[i-4] 모두가 상근이가 나와야만 창영이가 이길 수 있다 (!) -> 이게 핵심포인트 !!!
N = int(input())
dp = [1, 1, 0, 1, 1]
for i in range(5, N+1):   
  if dp[i-1] + dp[i-3] + dp[i-4] == 3:
    dp.append(0)
  else:
    dp.append(1)

if dp[N] == 1: print("SK")
else: print("CY")