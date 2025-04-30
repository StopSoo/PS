# https://www.acmicpc.net/problem/20365

# 답안 1
# 걸린 시간: 96ms
# 딕셔너리를 활용한 풀이.
import sys
input = sys.stdin.readline

N = int(input())
problems = input().strip()

def solution(N, problems):
  colors = {'R': 0, 'B': 0}
  colors[problems[0]] = 1

  for i in range(1, N):
    if problems[i] != problems[i-1]: # 연속되지 않을 경우 체크
      colors[problems[i]] += 1
  return min(colors['R'], colors['B']) + 1

print(solution(N, problems))

# 답안 2
# B와 R을 기준으로 2개의 리스트를 만들어서 분리.
import sys
input = sys.stdin.readline

N = int(input())
problems = input().strip()

def solution(problems):
  rDatas = [v for v in problems.split('R') if v]
  bDatas = [v for v in problems.split('B') if v]

  return min(len(rDatas) + 1, len(bDatas) + 1)

print(solution(problems))