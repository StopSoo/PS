# https://www.acmicpc.net/problem/11004

# 내 답안
# 걸린 시간: 3696ms
import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
numbers = sorted(map(int, input().strip().split()))
print(numbers[K-1])