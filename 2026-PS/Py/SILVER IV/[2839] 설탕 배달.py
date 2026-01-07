# https://www.acmicpc.net/problem/2839
# 260107 풀이
# 알고리즘: DP
# 시간: 48ms

N = int(input())
answers = []
if N >= 5 and N % 5 == 0: answers.append(N // 5)
if N >= 3 and N % 3 == 0: answers.append(N // 3)

for i in range(1, N//5 + 1): 
  if N > 5 and (N - 5 * i) % 3 != 0: continue
  answers.append(i + (N - 5 * i) // 3)

print(-1) if answers == [] else print(min(answers))