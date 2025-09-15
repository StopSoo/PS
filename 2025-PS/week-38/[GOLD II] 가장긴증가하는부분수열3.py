# https://www.acmicpc.net/problem/12738

# 내 답안
# 걸린 시간: 4552ms(python3) / 520ms(pypy3)
# 알고리즘: 이진 탐색

# 12015_가장긴증가하는부분수열2 문제랑 같은 코드인데 ... 뭐가 다를까?
# 2번 문제와 다른 점: A 배열에 들어갈 수 있는 값의 범위가 다르다.
# 2번 문제는 3번 문제보다 값의 범위가 더 작고 양수만 가능해서 DP로도 풀 수 있음.
# 3번 문제는 값 자체가 음수가 가능하기도 하고, 범위가 너무 넓어서 값을 배열 인덱스로 활용하는 방식이 불가능. 
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