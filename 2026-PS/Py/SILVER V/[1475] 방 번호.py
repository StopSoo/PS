# https://www.acmicpc.net/problem/1475
# 260128 풀이
# 알고리즘: 구현
# 시간: 44ms

import sys
input = sys.stdin.readline

number = input().strip()
answer = 0
sn = 0 # 6, 9의 개ㅜ
for num in range(10):
    if num == 6 or num == 9:
        sn += number.count(str(num))
    else:
        answer = max(answer, number.count(str(num)))
print(max(answer, (sn + 1) // 2))