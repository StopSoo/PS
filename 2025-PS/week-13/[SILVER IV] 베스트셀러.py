# https://www.acmicpc.net/problem/1302

# 내 답안
# 걸린 시간: 36ms
# 문자열 / 해시를 사용한 집합과 맵 / 정렬
import sys
input = sys.stdin.readline

N = int(input().strip())
dt = dict()
for _ in range(N):
  book = input().strip()
  dt[book] = dt.get(book, 0) + 1
print(sorted(dt, key=lambda x: (-dt[x], x))[0])