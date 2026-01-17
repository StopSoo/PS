# https://www.acmicpc.net/problem/2606
# 260117 풀이
# 알고리즘: 그래프 탐색(BFS)

# 25년 3월에 작성한 코드
# 시간: 36ms
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
    global virus
    
    for line in lines[number]:
        if line == 1: continue
        if line not in virus:
            virus.append(line)
            find_virus(line)
        else: 
            continue

find_virus(1) # 1번 컴퓨터부터 시작
print(len(virus))

# 26년 1월에 작성한 코드
# 시간: 60ms
from collections import defaultdict, deque

n = int(input())
t = int(input())
graph = defaultdict(list)
for _ in range(t):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# BFS
deq = deque([1])
visited = [False] * (n + 1)
visited[1] = True
while deq:
    now = deq.popleft()
    
    if not visited[now]: visited[now] = True
    for node in graph[now]:
        if not visited[node]:
            deq.append(node)
            visited[node] = True

print(sum(visited) - 1)
