# https://www.acmicpc.net/problem/11656

# 내 답안
# 걸린 시간: 40ms
S = input()
answer = []
for i in range(len(S)):
  answer.append(S[i:])
answer.sort()
print(*answer, sep='\n')