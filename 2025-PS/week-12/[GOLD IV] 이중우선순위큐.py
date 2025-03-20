# https://www.acmicpc.net/problem/7662

# 답안
# 걸린 시간: 2032ms (pypy3)
# 힙을 따로 만들라는 힌트를 겟해서 풀이 !! but 어떻게 해도 시간 초과가 나서 gpt와 구글링을 ~...
# dictionary는 데이터의 탐색/제거가 O(1)만에 가능하므로, 이를 두 힙의 동기화에 사용한다 (!)
# 동기화 파트 -> count 딕셔너리는 항상 현재 상태를 유지. 
# 따라서 최대 힙에서 최댓값을 뺄 때, 최소 힙에서 최솟값을 뺄 때 그 값이 유효한 값인지 확인하는 과정이 필요.
import heapq
import sys
input = sys.stdin.readline
print = sys.stdout.write
# 삭제할 데이터가 있는지 체크하는 함수
def isEmpty(count):
  for item in count:
    if item[1] > 0: # 해당 값의 개수가 1 이상이라면 바로 False를 반환
      return False
  return True

T = int(input())
for _ in range(T):
  min_q = [] # 최소 힙
  max_q = [] # 최대 힙
  count = {} # 값 개수를 저장하는 딕셔너리 
  k = int(input())
  
  for _ in range(k):
    orders = input().strip().split()
    num = int(orders[1])

    if orders[0] == 'I': # 삽입
      if num in count: # 중복 삽입일 경우
        count[num] += 1
      else: # 처음 삽입일 경우
        heapq.heappush(min_q, num)
        heapq.heappush(max_q, -num)
        count[num] = 1
    elif orders[0] == 'D': # 삭제 
      if not isEmpty(count.items()): # 큐가 비어있지 않을 때
        if num == 1: # 최댓값 삭제
          while (-max_q[0] not in count) or (count[-max_q[0]] < 1): # 큐와 max_q를 동기화
            temp = -heapq.heappop(max_q)
            if temp in count: del(count[temp])
          count[-max_q[0]] -= 1 # 여기서 말하는 max_q[0]은 유효한 최댓값 (!)
        else: # 최솟값 삭제
          while (min_q[0] not in count) or (count[min_q[0]] < 1): # 큐와 min_q를 동기화
            temp = heapq.heappop(min_q)
            if temp in count: del(count[temp])
          count[min_q[0]] -= 1 # 여기서 말하는 min_q[0]은 유효한 최솟값 (!)
  
  if isEmpty(count.items()): 
    print("EMPTY\n")
  else:
    # 동기화
    while (min_q[0] not in count) or (count[min_q[0]] < 1):
      temp = heapq.heappop(min_q)
    while (-max_q[0] not in count) or (count[-max_q[0]] < 1):
      temp = -heapq.heappop(max_q)
    print(str(-max_q[0]) + ' ' + str(min_q[0]) + '\n')