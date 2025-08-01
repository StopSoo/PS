# https://www.acmicpc.net/problem/9252

# 내 답안
# 걸린 시간: 416ms
# 알고리즘: DP / 최장공통부분수열문제 / 문자열
# 아이디어: DP 테이블을 만들고 후에 LCS를 역추적한다(!)
w1 = input()
w2 = input()
l1, l2 = len(w1), len(w2)
w1, w2 = " " + w1, " " + w2 # 1 기반 인덱스
lcs = ""
# DP 테이블 먼저 만들기
dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
for i in range(1, l1 + 1):
  for j in range(1, l2 + 1):
    if w1[i] == w2[j]:
      dp[i][j] = dp[i-1][j-1] + 1
    else:
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# lcs 역추적하기 (!)
i, j = l1, l2
while i > 0 and j > 0:
  if w1[i] == w2[j]: 
    lcs += w1[i]
    i -= 1
    j -= 1
  else:
    if dp[i-1][j] >= dp[i][j-1]: i -= 1
    else: j -= 1

print(dp[l1][l2])
print(lcs[::-1])