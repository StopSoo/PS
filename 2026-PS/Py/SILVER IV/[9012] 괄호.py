# https://www.acmicpc.net/problem/9012
# 260105 풀이
# 자료구조: 스택
# 시간: 40ms
import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    str = input().strip()
    arr = []
    for j in range(len(str)):
        if len(arr) == 0:
            arr.append(str[j])
        else:
            if str[j] == "(": 
                arr.append(str[j])
            else:
                if arr[-1] == "(": arr.pop()
                else: arr.append(str[j])

    if not arr: print("YES")
    else: print("NO")

# 개선된 답안
import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    str = input().strip()
    stack = []
    flag = True
    for ch in str:
        if ch == "(": stack.append(ch)
        else:
            if stack: stack.pop()
            else: # 중간 중단함으로써 시간 절약
                flag = False
                break
    print("NO" if (not flag or stack) else "YES") # 조건 분기가 깖끔!
