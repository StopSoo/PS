# https://www.acmicpc.net/problem/1193
# 260130 풀이
# 알고리즘: 구현 / 수학
# 시간: 

import sys
input = sys.stdin.readline

X = int(input())
line = 1

while X > line: # 몇 번째 줄인지 체크
    X -= line
    line += 1
# 라인의 홀/짝 여부에 따라 분수가 채워지는 방향이 반대이다.
if line % 2 == 0:
    up = X
    down = line - X + 1
else:
    up = line - X + 1
    down = X

print(f'{up}/{down}')