# https://www.acmicpc.net/problem/10810

# 내 답안
N, M = map(int, input().split())
result = [0] * N
for m in range(M):
    i, j, k = map(int, input().split())
    for ind in range(i-1, j): result[ind] = k
print(' '.join(map(str, result)))