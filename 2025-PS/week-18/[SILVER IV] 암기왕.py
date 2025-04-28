# https://www.acmicpc.net/problem/2776

# 내 답안
# 해시를 사용한 집합과 맵 -> 딕셔너리 사용.
# 걸린 시간: 2072ms
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  dt = dict()
  n = int(input())
  ylist = sorted(map(int, input().strip().split()))
  for number in ylist: dt[number] = 1

  m = int(input())
  dlist = list(map(int, input().strip().split()))
  for number in dlist:
    if dt.get(number, 0) != 0: print(1)
    else: print(0)

# 이분 탐색으로 풀이.
# 걸린 시간: 6268ms
# 이분 탐색 시 left, right 꼭 추가하기 (!)
import sys
input = sys.stdin.readline

def search(lst, find, left, right):
  if left > right: return 0

  mid = (left + right) // 2
  if lst[mid] == find: return 1
  elif lst[mid] > find: return search(lst, find, left, mid-1)
  else: return search(lst, find, mid+1, right)

T = int(input())
for _ in range(T):
  n = int(input())
  ylist = sorted(map(int, input().strip().split()))
  m = int(input())
  dlist = list(map(int, input().strip().split()))
  for number in dlist:
    print(search(ylist, number, 0, n-1))

# 집합과 in 연산자를 활용한 답안.
# 걸린 시간: 1428ms
# 이게 제일 오래 걸릴 거라고 생각했는데 제일 빨랐음.
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  n = int(input())
  yset = set(map(int, input().strip().split()))
  m = int(input())
  dlist = list(map(int, input().strip().split()))
  for number in dlist:
    print(1 if number in yset else 0)