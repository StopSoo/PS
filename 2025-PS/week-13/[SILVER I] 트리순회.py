# https://www.acmicpc.net/problem/1991

# 내 답안
# 걸린 시간: 36ms
# 풀긴 풀었는데 뭔가 깔끔하다고는 생각이 안 듬
def preorder(graph, start): # 전위순회
  global ans_pre

  ans_pre += start
  for node in graph[start]:
    if node == '.': continue
    preorder(graph, node)

def inorder(graph, start): # 중위 순회
  global ans_inorder, visited

  for i, node in enumerate(graph[start]):
    if i == 0: # 왼쪽 자식
      if node == ".": continue
      if not visited[ord(node)-65]: 
        inorder(graph, node)
    if not visited[ord(start)-65]: ans_inorder += start
    visited[ord(start)-65] = True # 방문 체크
    if i == 1: # 오른쪽 자식
      if node == ".": continue
      inorder(graph, node)

def postorder(graph, start): # 후위순회
  global ans_post

  for node in graph[start]:
    if node == ".": continue
    postorder(graph, node)
  ans_post += start

N = int(input())
graph = dict()
for _ in range(N):
  root, left, right = input().split()
  graph[root] = [left, right]

ans_pre = ''
preorder(graph, 'A')
print(ans_pre)

ans_inorder = ''
visited = [False]*26
inorder(graph, 'A')
print(ans_inorder)

ans_post = ''
postorder(graph, 'A')
print(ans_post)

# 내가 원한 깔끔한 느낌의 답안
# 걸린 시간: 32ms (시간 면에서는 별로 차이가 없으나, 가독성 면에서 훨씬 뛰어남)
import sys
input = sys.stdin.readline

N = int(input().strip())
tree = {}
for _ in range(N):
  node, left, right = input().split()
  tree[node] = (left, right)

preorder_result, inorder_result, postorder_result = [], [], []

def preorder(node):
  if node == '.':
    return
  preorder_result.append(node)
  preorder(tree[node][0])
  preorder(tree[node][1])

def inorder(node):
  if node == '.':
    return
  inorder(tree[node][0])
  inorder_result.append(node)
  inorder(tree[node][1])

def postorder(node):
  if node == '.':
    return
  postorder(tree[node][0])
  postorder(tree[node][1])
  postorder_result.append(node)

preorder('A')
inorder('A')
postorder('A')

print("".join(preorder_result))
print("".join(inorder_result))
print("".join(postorder_result))