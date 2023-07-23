import sys

n = int(input())
ans = [-1] * n      # 오큰수 저장 배열을 애초에 -1로 초기화 
A = list(map(int, input().split()))
myStack = []

for i in range(n):
    while myStack and A[myStack[-1]] < A[i]:    # 오큰수 조건
        ans[myStack.pop()] = A[i]   # 정답 리스트에 오큰수 저장
    myStack.append(i)

print(*ans)