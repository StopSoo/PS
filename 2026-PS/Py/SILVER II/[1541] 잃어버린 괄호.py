# https://www.acmicpc.net/problem/1541
# 260105 풀이
# 자료구조: 문자열
# 시간: 48ms

import sys
input = sys.stdin.readline

equation = input()
exp = equation.split('-')
result = sum(map(int, exp[0].split('+')))
for e in exp[1:]:
    result -= sum(map(int, e.split('+')))
print(result)