# https://www.acmicpc.net/problem/1068

# 내 답안
# 걸린 시간: 56ms
# 알고리즘: 트리
# 1. 트리 구성 시 defaultdict 사용하기
# 2. 실제로 트리에서 삭제하기보다는 삭제 체크 후 확인하는 방식이 낫다. -> O(1)
# 3. DFS로 리프 노드 체크하는 방식 익히기
from collections import defaultdict  
import sys
sys.setrecursionlimit(1000000)

N = int(input())
nodes = list(map(int, input().split()))
tree = defaultdict(list)
removed_node = int(input()) # 지울 노드
checked = [0] * N

for child, parent in enumerate(nodes):
  if parent != -1: tree[parent].append(child)
  else: root = child # 루트 노드 저장

def dfs_delete(start):
  checked[start] = 1 # 삭제 체크
  for child in tree[start]:
    dfs_delete(child)

def dfs_check(current):
  if checked[current]: return 0 # 삭제된 애라면 pass
  if not tree[current] or all(checked[child] for child in tree[current]):
    return 1 # 리프 노드일 경우
  
  cnt = 0
  for child in tree[current]:
    cnt += dfs_check(child)
  return cnt

dfs_delete(removed_node) # 삭제할 노드 체크
# 리프 노드 개수 세기 
if removed_node == root: print(0)
else: print(dfs_check(root))