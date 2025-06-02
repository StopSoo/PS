# https://www.acmicpc.net/problem/2780

# 답안
# 걸린 시간: 68ms
# 첫 코드 시간 초과 남 -> BFS는 돌리는데 이 결과를 다음 결과 계산 시 이용하지 않기 때문에 최적화가 안됨.
# 최종 코드 최적화 ok -> BFS 로직을 이용해서 DP에 적용 (!!)
graph = {1: [2, 4], 2: [1, 3, 5], 3: [2, 6], 4: [1, 5, 7], 5: [2, 4, 6, 8], 6: [3, 5, 9], 7: [4, 8, 0], 8: [5, 7, 9], 9: [6, 8], 0: [7]}
MOD = 1234567

T = int(input())
ns = list(int(input()) for _ in range(T))
dp = [[0] * 10 for _ in range(max(ns) + 1)]
for i in range(10): dp[1][i] = 1 # 한 자리 비밀번호는 각 숫자 한 개씩 존재
for i in range(2, max(ns) + 1):
  for j in range(10):
    for neighbor in graph[j]:
      dp[i][j] = (dp[i][j] + dp[i-1][neighbor]) % MOD
# 출력
for n in ns: print(sum(dp[n]) % MOD)