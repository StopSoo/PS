# https://www.acmicpc.net/problem/2231

# 내 답안
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().strip())
answer = 0
for num in range(1, N+1):
  result = num
  for n in str(num): result += int(n)
  if result == N: 
    answer = num
    break
print(str(answer) + '\n')

# 짧은 시간복잡도를 가지는 코드
# 문자열은 탐색이 되므로 ~~
N = int(input())  
for M in range(1, N + 1):
  sum_M = M + sum(map(int, str(M))) # 체크 (!)
  if sum_M == N: 
    print(M) 
    break 
else:
  print(0)