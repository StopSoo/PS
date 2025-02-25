# https://www.acmicpc.net/problem/2606

# 내 답안
# 걸린 시간: 36ms
import sys
input = sys.stdin.readline

total = int(input().strip())
N = int(input().strip())
lines = dict()
for i in range(total): lines[i+1] = [] # 초기화 
for _ in range(N): # 그래프 만들기
  c1, c2 = map(int, input().strip().split())
  lines[c1] += [c2]
  lines[c2] += [c1]

virus = [] 
def find_virus(number):
  global virus # global 선언 (!)
  
  for line in lines[number]:
    if line == 1: continue
    if line not in virus:
      virus.append(line)
      find_virus(line)
    else: 
      continue

find_virus(1) # 1번 컴퓨터부터 시작
print(len(virus))

# DFS를 활용한 답안
import sys
input = sys.stdin.readline

num = int(input())
edges = int(input())

graph = [[] for _ in range(num + 1)]
visited = [False] * (num + 1) # 방문 체크 배열

for i in range(edges):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(i):
  visited[i] = True
  for neighbors in graph[i]:
    if visited[neighbors]==False:
      dfs(neighbors)

dfs(1)
print(visited.count(True)-1) # 컴퓨터 1번 제외