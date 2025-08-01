# https://www.acmicpc.net/problem/9251

# 내 답안
# 걸린 시간: 376ms
# 알고리즘: 최장공통부분수열 문제 / DP
# 핵심 원리: 문자열1의 i번째 문자와 문자열2의 j번째 문자가 같으면 문자열1의 (i-1)번째까지의 문자열과 문자열2의 (j-1)번째까지의 문자열의 LCS에 1을 더한다.
str1 = input()
str2 = input()
l1, l2 = len(str1), len(str2)
str1, str2 = " " + str1, " " + str2 # 1 기반 인덱스를 위함

dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
for i in range(1, l1 + 1):
  for j in range(1, l2 + 1):
    if str1[i] == str2[j]:
      dp[i][j] = dp[i-1][j-1] + 1
    else:
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[l1][l2])