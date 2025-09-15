# https://www.acmicpc.net/problem/14003

# 내 답안
# 걸린 시간: 5300ms
# 알고리즘: 이진 탐색 & 역추적 -> 실제 LIS 배열을 찾아야 하므로 역추적을 반드시 해야 함(!!!)
# 1~3번 문제는 실제 LIS를 찾은 게 아니라, LIS 길이를 구하기 위한 후보 배열을 구한 거라 실제 LIS 배열과는 차이가 있음 (!)
import sys
input = sys.stdin.readline

N = int(input().strip())
numbers = list(map(int, input().strip().split()))

lis = []
indexs = [0] * N # lis 배열 상에서 몇 번째 위치에 들어가는지 기록 (!) -> dp 대체용?
for i in range(N):
  if not lis or lis[-1] < numbers[i]:
    lis.append(numbers[i])
    indexs[i] = len(lis) - 1 # 인덱스 기록
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
    indexs[i] = low # 인덱스 기록

# 역추적하기
len_lis = len(lis)
current_length = len_lis - 1 # 인덱스 기반이라서
answer = [] # 진짜 LIS
for i in range(N-1, -1, -1):
  if indexs[i] == current_length and (not answer or numbers[i] <= answer[-1]):
    answer.append(numbers[i])
    current_length -= 1

answer.reverse()
print(len_lis)
print(*answer)