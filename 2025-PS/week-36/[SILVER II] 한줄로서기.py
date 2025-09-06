# https://www.acmicpc.net/problem/1138

# 내 답안
# 걸린 시간: 36ms
# 알고리즘: 그리디 -> 근데 그리디 아닌 것 같다는 반응이 있음.
# 약간 "빈 자리 찾기"?
N = int(input())
info = list(map(int, input().split()))
pos = [0] * N

for number, ind in enumerate(info, start=1):
  cnt = ind
  for i in range(N):
    if cnt == 0 and pos[i] == 0: # 자리 배정
      pos[i] = number 
      number += 1
      break

    if pos[i] == 0:
      cnt -= 1     

print(*pos)