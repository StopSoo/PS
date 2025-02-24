# https://www.acmicpc.net/problem/1966

# 내 답안
# 걸린 시간: 88ms
# deque - append(값) / pop(): 맨 마지막에 추가 / 맨 마지막 원소를 제거 (순서가 정해져있음)
# deque - insert(인덱스, 값) / remove(인덱스, 값): 원하는 위치의 값을 추가/제거 가능
# 풀이 포인트(1): 선택한 인덱스의 값을 어떻게 표시할지 -> deque에 튜플로 인덱스를 같이 저장하기
# 풀이 포인트(2): 튜플들로 이루어진 리스트에서 최댓값을 어떻게 구할지 -> 람다 함수를 이용하기
# 풀이 포인트(3): deque 왼쪽에서 값을 빼서 오른쪽에 다시 넣을 때 -> rotate() 사용하기
from collections import deque

T = int(input())
for test in range(T):
  N, M = map(int, input().split())
  numbers = list(map(int, input().split()))
  queue = deque([(num, i == M) for i, num in enumerate(numbers)])

  count = 1 # 인쇄 순서
  while True:
    if queue[0][1] and queue[0][0] == max(queue, key=lambda x: x[0])[0]:
      print(count)
      break
    elif queue[0][0] == max(queue, key=lambda x: x[0])[0]: 
      count += 1
      queue.popleft()
    else:
      queue.rotate(-1)