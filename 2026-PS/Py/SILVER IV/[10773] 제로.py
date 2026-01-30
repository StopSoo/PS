# https://www.acmicpc.net/problem/10773
# 260130 풀이
# 알고리즘: 구현 / 자료구조(스택)
# 시간: 72ms

import sys
input = sys.stdin.readline

K = int(input())
stack = []
for _ in range(K):
    number = int(input().strip())
    if number: stack.append(number)
    else: stack.pop()

print(sum(stack))