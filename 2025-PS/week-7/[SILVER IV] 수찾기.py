# https://www.acmicpc.net/problem/1920

# 내 답안
# 걸린 시간: 120ms
# set1, set2 모두 list 자료형으로 했을 때 시간 초과 남
# 순서를 유지해야 하는 set2만 list로 놔두고, set1만 set으로 변경 (!) => O(N)에서 O(1)로 단축됨
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().strip())
set1 = set(map(int, input().strip().split()))
M = int(input().strip())
set2 = list(map(int, input().strip().split()))

for number in set2: print('1\n' if number in set1 else '0\n')

# 이진 탐색으로 풀기
def binary_search(arr, target):
  left, right = 0, len(arr) - 1 # 인덱스
  
  while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] > target:
      right = mid - 1
    else:
      left = mid + 1 
  return -1

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

arr.sort() # 이진 탐색하려면 배열이 정렬되어 있어야 함

for i in nums:
  if binary_search(arr, i) != -1: print(1)
  else: print(0)