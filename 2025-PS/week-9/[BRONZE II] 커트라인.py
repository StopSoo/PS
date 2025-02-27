# https://www.acmicpc.net/problem/25305

# 내 답안
# 걸린 시간: 36ms
N, k = map(int, input().split())
scores = sorted(list(map(int, input().split())), reverse=True)
print(scores[k-1])