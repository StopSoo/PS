# https://www.acmicpc.net/problem/1158

# 내 답안
# 걸린 시간: 56ms
from collections import deque

N, K = map(int, input().split())
people = deque(list(range(1, N+1)))

answer = []
while people:
  people.rotate(-(K-1)) # 왼쪽으로 두 칸 이동 (Ex> 1 -> 3)
  answer.append(str(people.popleft()))
print("<" + ', '.join(answer) + ">")