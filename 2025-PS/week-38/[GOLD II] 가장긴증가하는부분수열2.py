# https://www.acmicpc.net/problem/12015

# 내 답안
# 걸린 시간: 4388ms(python3) / 504ms(pypy3)
# 알고리즘: 이진 탐색
# 헷갈리고 어려웠던 점: 이진 탐색 구현 시 인덱스를 설정하는 부분
# 기본 아이디어: 가장 긴 증가하는 부분 수열을 만들기 위해서는, lis 배열의 마지막 원소가 최대한 작아야 함 (!)
import sys
input = sys.stdin.readline

N = int(input().strip())
numbers = list(map(int, input().strip().split()))

lis = []
for i in range(N):
  if not lis or lis[-1] < numbers[i]:
    lis.append(numbers[i])
  elif lis[-1] >= numbers[i]:
    # 이진 탐색
    low, high = 0, len(lis) - 1
    while low < high:
      mid = (low + high) // 2
      if lis[mid] < numbers[i]:
        low = mid + 1
      else: # 등호가 포함되어 있기 때문에 high를 mid로 설정해야 함 (!)
        high = mid
    lis[low] = numbers[i] # 교체

print(len(lis))