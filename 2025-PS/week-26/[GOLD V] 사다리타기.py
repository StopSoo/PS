# https://www.acmicpc.net/problem/2469

# 내 답안
# 걸린 시간: 36ms -> 40ms(로직 보완 후)
# 알고리즘: 시뮬레이션
# 아이디어: ????줄을 기점으로 전/후를 시뮬레이션한 후 두 상태를 비교해 정답을 도출한다.
import sys
input = sys.stdin.readline

k = int(input())
n = int(input())
before_pos = [chr(65 + alpha) for alpha in range(k)] # 감추어진 줄 전까지 시뮬레이션한 후 위치
after_pos = list(input().strip())

lines = [input().strip() for _ in range(n)] # 사다리
# 감추어진 줄 전까지 시뮬레이션
for line in lines: 
  if line == '?' * (k-1):
    break
  for i in range(k-1):
    if line[i] == '-':
      before_pos[i], before_pos[i+1] = before_pos[i+1], before_pos[i]
# 아래서부터 감추어진 줄 다음 줄까지 시뮬레이션
for line in lines[::-1]:
  if line == '?' * (k-1):
    break  
  for i in range(k-1):
    if line[i] == '-': 
      after_pos[i], after_pos[i+1] = after_pos[i+1], after_pos[i]

# 비교
result = '' # 제출할 정답 
is_valid = True  
i = 0
while i < k - 1:
  if before_pos[i] == after_pos[i]: 
    result += '*' 
    i += 1
  # 인접 swap이 가능한지를 체크(!)
  elif before_pos[i] == after_pos[i+1] and before_pos[i+1] == after_pos[i]: 
    result += '-'
    before_pos[i], before_pos[i+1] = before_pos[i+1], before_pos[i]
    i += 1
  else:
    is_valid = False              
    break

print(result if is_valid else 'x' * (k-1))