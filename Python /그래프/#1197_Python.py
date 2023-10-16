# 1197: 최소 스패닝 트리
# MST 개념을 이용한 기본 문제

import sys
from queue import PriorityQueue

input = sys.stdin.readline
N, M = map(int, input().split())  # 노드 개수, 에지 개수
pq = PriorityQueue()

# 부모 노드 배열을 선언하고 자기 자신으로 초기화
parent = [0] * (N+1)
for i in range(N+1):    
    parent[i] = i;  

# 주어진 에지 정보를 기준으로 에지 리스트에 값 삽입
for i in range(M):
    s, e, w = map(int, input().split()) # 시작 노드, 끝 노드, 가중치
    pq.put((w, s, e))   # 가중치를 기준으로 정렬하므로 가중치를 가장 먼저 해서 삽입

# Union-find에서 find 연산 
def find(a):
    if a == parent[a]:  # a가 대표 노드라면
        return a
    else:
        parent[a] = find(parent[a])     # 경로 압축을 위해 추가한 코드 (!) => 시간 복잡도 감소에 효과적
        return parent[a]

# Union-find에서 union 연산 
def union(a, b):
    # 부모 노드 찾기 
    a = find(a)
    b = find(b)

    if a != b:  # 아직 연결되어 있지 않다는 뜻 -> 연결해도 사이클이 생기지 않는다는 뜻
        parent[b] = a   # 연결

# main
useEdge = 0     # 사용한 에지 개수
result = 0      # 가중치 합

while useEdge < N-1:    # 사용한 에지 수가 (노드 수-1)이 될 떄까지 (!)
    w, s, e = pq.get()
    if find(s) != find(e):
        union(s, e)
        result += w
        useEdge += 1

print(result)