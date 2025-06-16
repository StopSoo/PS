# https://www.acmicpc.net/problem/2866

# 내 답안 + 효율성 개선
# 걸린 시간: 1080ms -> 580ms
# 알고리즘: 해시를 사용한 집합과 맵
# 자료구조: 문자열
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
words = list(input().strip() for _ in range(R))
columns = [''.join([words[j][i] for j in range(R)]) for i in range(C)]

count = 0
while True:
  seen = set()
  new_columns = []
  for col in columns:
    trimmed = col[1:]
    if trimmed in seen:
      print(count)
      exit(0)
    seen.add(trimmed)
    new_columns.append(trimmed)
  columns = new_columns # 갱신
  count += 1