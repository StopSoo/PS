# https://www.acmicpc.net/problem/10819

# 내 답안
# 걸린 시간: 112ms
def back():
  global N, answers, visited, numbers, results
  if len(answers) == N:
    s = 0
    for i in range(N-1): s += abs(answers[i]-answers[i+1])
    results.add(s)
    return

  for i in range(N):
    if not visited[i]:
      answers.append(numbers[i])
      visited[i] = True
      back()
      answers.pop()
      visited[i] = False

N = int(input())
numbers = list(map(int, input().split()))
visited = [False] * N
answers = [] # 식을 담는 배열
results = set() # 식의 계산값들을 담는 집합

back()
print(max(results))

# 백트래킹이 아니라 순열을 사용한다면
# 걸린 시간: 72ms
from itertools import permutations

def solution():
  N = int(input())
  A = list(map(int, input().split()))
  max_diff_sum = 0

  for a in permutations(A, N):
    diff_sum = 0
    for i in range(N - 1):
      diff_sum += abs(a[i] - a [i + 1])
    max_diff_sum = max(diff_sum, max_diff_sum)
  
  return max_diff_sum

print(solution())