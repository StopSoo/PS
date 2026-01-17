# https://www.acmicpc.net/problem/1522
# 260117 풀이
# 알고리즘: 슬라이딩윈도우
# 시간: 36ms
import sys
input = sys.stdin.readline

s = input().strip()
a_count = s.count('a') # a의 개수가 윈도우의 사이즈

s = s + s # 운형 문자열이라 이어 붙임

min_ans = sys.maxsize # int의 최댓값
for i in range(len(s) - a_count):
    window = s[i:i + a_count]
    min_ans = min(min_ans, window.count('b'))
print(min_ans)