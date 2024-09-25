# 2869
import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())

count = 0
meter = 0
while meter < V:
    count += 1  # 횟수 1 증가
    meter += A  # 낮
    if meter >= V:
        break
    else:
        meter -= B  # 밤

print(count)

# 시간 초과 !!
# 복습할 때 단순 연산으로 풀 수 있는지 고민해볼 것