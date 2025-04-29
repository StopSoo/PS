# https://www.acmicpc.net/problem/10867

# 내 답안
# 걸린 시간: 52ms
N = int(input())
numbers = set(map(int, input().split()))
print(*sorted(numbers))