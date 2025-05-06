# https://www.acmicpc.net/problem/12933

# 답안
# 걸린 시간: 120ms
# 첫 코드: ori = ori[:i] + 'X' + ori[i+1:] 이렇게 매번 새로운 문자열을 할당하는 방식으로 했더니 시간 초과가 떴었음.
# 다시 나중에 차분히 복습해야 할 필요 있을 듯.
import sys
input = sys.stdin.readline 

sound = ['q', 'u', 'a', 'c', 'k']
ori = list(input().strip())
len_ori = len(ori)
count = 0 # 오리의 최소 수
flag = True
while True:
  if ori.count('X') == len_ori: break 

  pointer = 0
  progressed = False # 이전 루프에서 오리를 한 마리라도 처리했는지
  for i in range(len_ori):
    if ori[i] == sound[pointer]: 
      ori[i] = 'X'
      pointer += 1
      progressed = True
    if pointer == 5: pointer = 0 # 초기화
  if pointer != 0 or not progressed: 
    flag = False
    break

  count += 1

print(count if flag else -1)