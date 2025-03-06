# https://www.acmicpc.net/problem/9251

# 내 답안
# 걸린 시간: 428ms
# LCS: 최장 공통 부분 수열
# dp[n][m]: 인덱스 n까지의 문자열1과 인덱스 m까지의 문자열2을 살펴봤을 때의 LCS의 길이 
# Bottom-Up 방식 사용
# 인덱스가 0인 지점들을 0으로 초기화하면 초기값 처리 때 편하다 (!)
w1 = input()
w2 = input()

N, M = len(w1), len(w2)
w1, w2 = " " + w1, " " + w2 # 인덱스 1부터 시작임을 맞추기 위해 (!)
dp = [[0 for _ in range(M+1)] for _ in range(N+1)] # 안 쓰는 공간을 0으로 채우기
for i in range(1, N+1):
  for j in range(1, M+1):
    if w1[i] == w2[j]: # w1의 i번째 문자와 w2의 j번째 문자가 같으면 
      dp[i][j] = dp[i-1][j-1] + 1 # w1의 i-1번째까지의 문자열과 w2의 j-1번째까지의 문자열의 LCS에 1 더하기
    else:
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[N][M])