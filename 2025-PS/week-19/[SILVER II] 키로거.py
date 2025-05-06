# https://www.acmicpc.net/problem/5397

# 내 답안
# 걸린 시간: 824ms
# 처음에 시도한 방법: 커서 위치를 하나의 변수에 저장하고, 커서 위치에 문자 삽입/삭제 적용 -> 시간 복잡도 증가
# 최종 답안에 적용한 방식: 커서를 기준으로 왼쪽 스택과 오른쪽 스택을 구분해서 저장.
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  pw = input().strip()
  left, right = [], [] # 커서를 기준으로 왼쪽/오른쪽 스택 구분

  for ch in pw:
    if ch == '<':
      if left: right.append(left.pop())
    elif ch == '>':
      if right: left.append(right.pop())
    elif ch == '-':
      if left: left.pop()
    else: left.append(ch) # 문자와 숫자 모두
  left.extend(reversed(right)) # 뒤집어서 추가해야한다는 점(!)
  print(''.join(left))