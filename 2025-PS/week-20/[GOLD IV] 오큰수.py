# https://www.acmicpc.net/problem/17298

# 내 답안
# 걸린 시간: 1056ms
# 일반적인 이중 for문으로는 시간 초과가 나서 풀지 못함 !!
# 스택 활용 -> 오큰수를 찾지 못했더라도 스택에 인덱스를 넣어야 후 턴에서 찾을 수 있음 (!)
import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().strip().split()))

stack = [] # 인덱스를 담을 스택
answer = [-1] * N # 오큰수가 없을 때 넣을 값인 -1로 초기화

stack.append(0) # 인덱스 0부터 시작
for i in range(1, N):
  while stack and numbers[stack[-1]] < numbers[i]:
    answer[stack.pop()] = numbers[i]
  stack.append(i) 

print(*answer)