# https://www.acmicpc.net/problem/14248

# 내 답안
# 걸린 시간: 52ms
# 알고리즘: DFS
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(now):
  global checked, n
  
  checked[now] = 1
  for jump in (now - A[now], now + A[now]):
    if 1 <= jump <= n and not checked[jump]:
      dfs(jump)

n = int(input().strip())
A = [0] + list(map(int, input().split()))
s = int(input())

checked = [0] * (n + 1)
dfs(s)
print(sum(checked))