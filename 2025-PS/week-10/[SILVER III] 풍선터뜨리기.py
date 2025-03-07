# https://www.acmicpc.net/problem/2346

# 내 답안
# 걸린 시간: 56ms
# 문제를 꼼꼼히 읽고 제대로 파악하자 !!
from collections import deque

deq = deque()
N = int(input())
papers = list(map(int, input().split()))
for i, paper in enumerate(papers): deq.append((paper, i+1))
answers = []
while deq:
  pop_number = deq.popleft()
  answers.append(pop_number[1])
  if pop_number[0] > 0: deq.rotate(-pop_number[0]+1)
  else: deq.rotate(-pop_number[0])
print(*answers)

# deq 선언, papers 선언 및 초기화, 인덱스 넣는 부분 모두 한 줄로 정리하기
# 인덱스가 0부터 시작하는 부분은 나중에 추가할 때 1 더하면 됨 !!
q = deque(enumerate(map(int, input().split())))