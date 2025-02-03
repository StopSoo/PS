# https://www.acmicpc.net/problem/11651

# 내 답안
N = int(input())
points = sorted([list(map(int, input().split())) for i in range(N)], key=lambda x: [x[1], x[0]])
for i in range(N): print(points[i][0], points[i][1])