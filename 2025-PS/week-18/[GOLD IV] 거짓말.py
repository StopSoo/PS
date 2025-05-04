# https://www.acmicpc.net/problem/1043

# 답안 1: 집합을 이용해 풀이.
# 걸린 시간: 36ms
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
knowList = set(input().strip().split()[1:])
parties = []

for _ in range(M): parties.append(set(input().strip().split()[1:]))
# knowList 업데이트
for _ in range(M):
  for party in parties:
    if party & knowList: # 둘의 교집합이 있다면
      knowList = knowList.union(party) # 둘의 합집합으로 업데이트

cnt = 0
for party in parties:
  if party & knowList: continue
  cnt += 1

print(cnt)

# 답안 2: 그래프로 풀이 (BFS)
# 걸린 시간:
from sys import stdin
sys.setrecursionlimit(10000)

n, m = map(int, stdin.readline().split())
truth = set(stdin.readline().split()[1:])
parties = []
graph = { str(i): [] for i in range(1, n+1) }

for _ in range(m): # 같은 파티에 참석한 사람들끼리는 그래프에서 연결되어있다고 가정.
  party = stdin.readline().split()[1:]
  parties.append(party)
  for i in range(len(party)):
    for j in range(i+1, len(party)):
      graph[party[i]].append(party[j])
      graph[party[j]].append(party[i])

visited = set()

def dfs(node):
  visited.add(node)
  for neighbor in graph[node]:
    if neighbor not in visited:
      dfs(neighbor)
# 진실을 아는 사람들에서 DFS로 연결된 모든 사람 탐색
for person in truth: dfs(person)

cnt = 0
for party in parties:
  if all(p not in visited for p in party):
    cnt += 1

print(cnt)