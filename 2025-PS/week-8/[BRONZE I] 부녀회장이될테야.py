# https://www.acmicpc.net/problem/2775

# 내 답안
# 걸린 시간: 32ms
# 첫 코드(재귀 함수) -> 시간 초과
# 두 번째 코드(memoization) -> good
# (*) 주의할 점: 리스트에서 += 연산 사용할 때 리스트를 더해야 함 !!
import sys
input = sys.stdin.readline

# def get_count_people(k, n):
#   if k == 0: return n
#   return sum([get_count_people(k-1, i) for i in range(1, n+1)])

people = [[] for _ in range(15)]
for i in range(15):
  if i == 0: people[i] = [num for num in range(1, 15)]
  else:
    for j in range(14):
      people[i] += [sum(people[i-1][0:j+1])] 

T = int(input().strip())
for _ in range(T):
  k = int(input().strip())
  n = int(input().strip())
  print(people[k][n-1])