# https://www.acmicpc.net/problem/10828
# 260107 풀이
# 알고리즘: 자료구조/스택
# 시간: 44ms

import sys
input = sys.stdin.readline

N = int(input().strip())
stack = []
size = 0
for _ in range(N):
    order = input().strip().split()
    if order[0] == 'push':
        stack.append(order[1])
        size += 1
    elif order[0] == 'pop':
        if stack: 
            number = stack.pop()
            print(number)
            size -= 1
        else: print(-1)
    elif order[0] == 'size':
        print(size)
    elif order[0] == 'empty':
        print(1 if size == 0 else 0)
    elif order[0] == 'top':
        print(stack[-1] if stack else -1)