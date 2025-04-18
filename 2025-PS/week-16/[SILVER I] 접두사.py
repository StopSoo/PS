# https://www.acmicpc.net/problem/1141

# 내 답안
# 걸린 시간: 40ms
# 정렬 기준을 len으로 해서 순차적으로 확인하는 방법도 있음!!
import sys
input = sys.stdin.readline

N = int(input())
words = sorted([input().strip() for _ in range(N)])

valid = [True] * N  # 살아남은 단어 표시
for i in range(N):
  if not valid[i]: continue
  for j in range(N):
    if i == j: continue
    if words[j].startswith(words[i]) and words[j] != words[i]:
      valid[i] = False
# 중복 단어 고려
print(len(set(words[idx] for idx, value in enumerate(valid) if value)))
