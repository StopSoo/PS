# https://www.acmicpc.net/problem/11582

# 내 답안
# 걸린 시간: 1000ms
# 알고리즘: 분할정복 -> 병합정렬로 시도
# 하지만 파이썬이라 너무 쉬웠음 ... 
import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
k = int(input())

for i in range(0, N, N//k):
  numbers[i:i+N//k] = sorted(numbers[i:i+N//k])
print(*numbers)