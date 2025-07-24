# https://www.acmicpc.net/problem/11441

# 내 답안
# 걸린 시간:
import sys
input = sys.stdin.readline

N = int(input())
numbers = [0] + list(map(int, input().split()))
M = int(input())
ts = [list(map(int, input().split())) for _ in range(M)]

for i in range(1, N+1): numbers[i] += numbers[i-1] # 누적합
for i, j in ts: print(numbers[j] - numbers[i-1]) # 출력