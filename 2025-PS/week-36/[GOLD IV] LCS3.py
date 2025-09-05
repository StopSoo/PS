# https://www.acmicpc.net/problem/1958

# 내 답안
# 걸린 시간: 568ms
# 알고리즘: DP
# LCS를 두 번 하는 건 어때? -> 틀림
# 아이디어: 3차원 배열로 DP를 하라. 
import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()
str3 = input().strip()

l1, l2, l3 = len(str1), len(str2), len(str3)
str1, str2, str3 = " " + str1, " " + str2, " " + str3 # 1 기반 인덱스

dp = [[[0] * (l3 + 1) for _ in range(l2 + 1)] for _ in range(l1 + 1)]
for i in range(1, l1 + 1):
  for j in range(1, l2 + 1):
    for k in range(1, l3 + 1):
      if str1[i] == str2[j] == str3[k]:
        dp[i][j][k] = dp[i-1][j-1][k-1] + 1
      else:
        dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

print(dp[l1][l2][l3])