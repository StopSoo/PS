# https://www.acmicpc.net/problem/2920

# 내 답안
numbers = list(map(int, input().split()))
if numbers == sorted(numbers): print('ascending')
elif numbers == sorted(numbers, reverse=True): print('descending')
else: print('mixed')