# https://www.acmicpc.net/problem/12101

# 내 답안
# 걸린 시간: 36ms
# 이 문제가 DP 카테고리에 있다는 점을 고려해서 아이디어를 짤 수 있다는 것을 (!)
# 튜플 더할 때 (1) 이렇게 하면 안되고, (1,) 이렇게 해야 한다는 거슬 ~~
# 이 문제를 백트래킹으로도 풀 수 있다는 거슬 ~~
# 게다가 이 코드는 중복이 많기 때문에 비효율적임
n, k = map(int, input().split())
dp = [
  [[1]], 
  [[1]], 
  [[1, 1], [2]],
  [[1, 1, 1], [1, 2], [2, 1], [3]],
]

if n >= 4: 
  for i in range(4, n+1):
    temp = []
    for l in dp[i-1]:
      temp.append(tuple(l) + (1,))
      temp.append((1,) + tuple(l))
    for l in dp[i-2]:
      temp.append(tuple(l) + (2,))
      temp.append((2,) + tuple(l))
    for l in dp[i-3]:
      temp.append(tuple(l) + (3,))
      temp.append((3,) + tuple(l))
    dp.append(sorted(map(list, set(temp))))
# print(dp[n])
if len(dp[n]) < k: print(-1)
else: print('+'.join(map(str, dp[n][k-1])))

# DFS를 활용해서 더 깔끔하게 작성한 답안
def dfs(n, path, result):
  if n == 0:
    result.append(path)
    return
  for i in [1, 2, 3]:
    if path and i < path[-1]:  # 오름차순 유지 (중복 방지)
      continue
    if n - i >= 0:
      dfs(n - i, path + [i], result)

n, k = map(int, input().split())
result = []
dfs(n, [], result)

if len(result) < k: print(-1)
else: print('+'.join(map(str, result[k-1])))