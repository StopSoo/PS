# https://www.acmicpc.net/problem/5639

# 내 답안
# 걸린 시간: 1940ms
# 자료구조: 트리/그래프
# 알고리즘: 재귀
# 1. 전위/중위 순회를 활용해서 후위 순회를 구하는 문제를 참고 (!)
# 2. 이진 검색 트리의 특징을 활용해 코드를 구현 (!)
# 3. EOF 입력 처리 복기하기 (MacOS는 Ctrl+D)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def find_postorder(s, e):
  global pre_order

  if s > e: return

  root = pre_order[s] # 루트 노드
  left_tree_size = 0
  for i in range(s + 1, e + 1):
    if pre_order[i] > root:
      left_tree_size = i - s - 1
      break
  # 왼쪽 트리 호출
  find_postorder(s + 1, s + left_tree_size)
  # 오른쪽 트리 호출
  find_postorder(s + left_tree_size + 1, e)
  # 루트 출력
  print(root)

pre_order = []
while True:
  number = input()
  if number == "": break  
  else: pre_order.append(int(number))

find_postorder(0, len(pre_order) - 1)
