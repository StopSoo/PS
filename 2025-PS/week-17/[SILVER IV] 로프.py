# https://www.acmicpc.net/problem/2217

# 내 답안
# 걸린 시간: 100ms
# 빠른 입출력을 사용하는 것이 속도 절감에 굉장한 도움이 됨 !!
import sys
input = sys.stdin.readline

N = int(input())
line = sorted(list(int(input().strip()) for _ in range(N)))
results = []
for i in range(N):
  results.append(line[i] * (N-i))
print(max(results))