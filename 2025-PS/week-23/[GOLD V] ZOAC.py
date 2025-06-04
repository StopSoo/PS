# https://www.acmicpc.net/problem/16719

# 내 답안
# 걸린 시간: 32ms
# 알고리즘: 분할정복 + 그리디
# 처음엔 어떻게 접근해야 하는지 감 잡기 어려웠음.
# 첫 코드에서 놓친 부분: 좌측 탐색 시 항상 0부터가 아니라 start부터 탐색해야 한다는 것 (!)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def solve(start, end):
  if start >= end: return

  min_char = min(word[start:end]) # 범위 내 문자 중 사전 순으로 가장 빠른 문자 반환
  idx = start + word[start:end].index(min_char)
  answer[idx] = min_char # 정답 배열에 문자 채워넣기
  print(''.join(answer))

  solve(idx + 1, end) # 우측
  solve(start, idx) # 좌측

word = input().strip()
len_word = len(word)
answer = ['' for _ in range(len_word)]
solve(0, len_word)