# https://www.acmicpc.net/problem/2263

# 내 답안
# 걸린 시간: 296ms
# 이 문제를 푸는 데 꼭 필요한 개념: postorder 리스트의 마지막 원소는 항상 루트 노드이다(!)
# 매번 index 함수를 활용하는 것보다 dict를 활용하는 것이 더 효율적임 !! (메모리 효율적)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def find_preorder(in_s, in_e, post_s, post_e):
  if in_s > in_e: return

  root = post_order[post_e]
  print(root, end=' ')
  
  root_index = inorder_index[root]
  left_size = root_index - in_s # 왼쪽 트리 사이즈
  # 왼쪽 재귀 호출
  find_preorder(in_s, root_index - 1, post_s, post_s + left_size - 1)
  # 오른쪽 재귀 호출
  find_preorder(root_index + 1, in_e, post_s + left_size, post_e - 1)

N = int(input())
in_order = list(map(int, input().strip().split()))
post_order = list(map(int, input().strip().split()))
inorder_index = {in_order[i]:i for i in range(N)} # 중위 순회 인덱스 O(1)

find_preorder(0, N-1, 0, N-1)