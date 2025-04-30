# https://www.acmicpc.net/problem/11497

# 내 답안
# 걸린 시간: 244ms
# 그리디 알고리즘 -> 높이들의 차이를 최소화하려면 낮은/높은 순으로 가운데부터 양끝쪽으로 번갈아 붙이기.
# 정렬 후 양 끝 배치 전략은 그리디 최적해로 잘 알려진 방식이다(!) -> 시간 복잡도 O(nlogn)
import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
answers = []
for _ in range(T):
  N = int(input())
  deq = deque() # 최적의 케이스로 배치한 배열
  heights = sorted(list(map(int, input().split())), reverse=True)
  for i in range(N):
    if i % 2 == 1: deq.appendleft(heights[i])
    else: deq.append(heights[i])
  answers.append(max([abs(deq[i] - deq[i+1]) for i in range(N-1)] + [abs(deq[0] - deq[-1])]))

print(*answers, sep='\n')

# 개선할 수 있는 부분
# 1. max값 구할 때 굳이 리스트 만들지 않고 for문 돌면서 max값 추적하기.
# 2. 역순 정렬 -> 굳이 역순 정렬 필요 X.
# 3. 리스트의 양쪽으로 번갈아 넣는 부분 -> 정렬된 리스트를 반으로 나눠서 합치는 방식으로 변경 가능.
# left = heights[::2]
# right = heights[1::2][::-1]
# final = left + right