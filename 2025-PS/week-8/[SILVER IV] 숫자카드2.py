# https://www.acmicpc.net/problem/10816

# 내 답안 -> 시간 초과
import sys
input = sys.stdin.readline
print = sys.stdout.write

def search(arr, target, start, end):
  while start <= end:
    mid = (start+end) // 2
    if arr[mid] == target:
      # list.count(값)을 사용하면 O(N)이 걸린다고 해서 이렇게 해봄 ...
      # 근데 list.index(값) 연산도 O(N)이 걸린다고 함 ... 
      start_index = arr[start:end+1].index(target)
      end_index = len(arr[start:end+1]) - arr[start:end+1][::-1].index(target) - 1
      return str(end_index - start_index + 1) + ' '
    elif arr[mid] > target: end = mid - 1
    else: start = mid + 1
  return '0 '

N = int(input().strip())
cards = sorted(list(map(int, input().strip().split()))) # 정렬
M = int(input().strip())
numbers = list(map(int, input().strip().split()))

for num in numbers:
  print(search(cards, num, 0, N-1))

# 해결 답안 -> bisect 활용하기 (!)
import sys
import bisect

input = sys.stdin.readline
print = sys.stdout.write

def count_by_bisect(arr, target):
  left_index = bisect.bisect_left(arr, target)  # target이 처음 등장하는 위치
  right_index = bisect.bisect_right(arr, target)  # target이 마지막으로 등장한 위치 + 1
  return str(right_index - left_index) + ' '  # 등장한 개수 반환

N = int(input().strip())
cards = sorted(map(int, input().strip().split()))  # 정렬
M = int(input().strip())
numbers = map(int, input().strip().split())

for num in numbers:
  print(count_by_bisect(cards, num))