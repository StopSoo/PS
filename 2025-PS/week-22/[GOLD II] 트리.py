# https://www.acmicpc.net/problem/4256

# 내 답안
# 걸린 시간: 240ms
# 2263_트리의 순회 문제 참고해서 풀이!!
# 트리 풀이 시 중요한 점 
# 1) 전위/후위 순회 때 루트의 위치 파악 가능
# 2) 중위 순회 인덱스를 미리 딕셔너리로 저장해서 시간 복잡도 줄이기
# 3) 재귀의 특징을 잘 활용할 것
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def find_postorder(pre_s, pre_e, in_s, in_e):
  if in_s > in_e: return

  root = pre_order[pre_s]
  root_index = inorder_index[root]
  left_tree_size = root_index - in_s # 왼쪽 트리 사이즈
  # 왼쪽 트리 호출
  find_postorder(pre_s + 1, pre_s + left_tree_size, in_s, root_index - 1)
  # 오른쪽 트리 호출
  find_postorder(pre_s + left_tree_size + 1, pre_e, root_index + 1, in_e)
  # 루트 출력
  print(root, end=' ') 

T = int(input())
for _ in range(T):
  n = int(input()) # 노드의 개수
  pre_order = list(map(int, input().strip().split()))
  in_order = list(map(int, input().strip().split()))
  inorder_index = {in_order[i]: i for i in range(n)} # 중위 순회 인덱스 조회 O(1)
  
  find_postorder(0, n-1, 0, n-1)
  print()