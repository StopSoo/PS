# https://www.acmicpc.net/problem/2908

# 내 답안
A, B = input().split()
print(A[::-1] if A[::-1] > B[::-1] else B[::-1])