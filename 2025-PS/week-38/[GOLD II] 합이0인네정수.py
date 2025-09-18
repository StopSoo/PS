# https://www.acmicpc.net/problem/7453

# 내 답안
# 걸린 시간: 시간 초과(python3) / 6968ms(pypy3)
# 알고리즘: 투포인터
# 감을 못 잡겠어서 풀이 흐름을 지피티한테 물어봄.
import sys
input = sys.stdin.readline

N = int(input().strip())
numbers = [[] for _ in range(4)]
for _ in range(N):
  abcd = list(map(int, input().strip().split()))
  for i in range(4):
    numbers[i].append(abcd[i])

AB, CD = [], []
for i in range(N):
  for j in range(N):
    AB.append(numbers[0][i] + numbers[1][j])
    CD.append(numbers[2][i] + numbers[3][j])

AB.sort()
CD.sort()

answer = 0
i, j = 0, N * N - 1
while i < N * N:
  if AB[i] == -CD[j]:
    # count 함수 쓰면 시간 초과 남
    val_ab, val_cd = AB[i], CD[j]
    cnt1, cnt2 = 0, 0
    while i < N * N and AB[i] == val_ab:
      i += 1
      cnt1 += 1
    while j >= 0 and CD[j] == val_cd:
      j -= 1
      cnt2 += 1
    answer += cnt1 * cnt2
  elif AB[i] > -CD[j]:
    if j > 0: j -= 1
    else: break
  elif AB[i] < -CD[j]:
    i += 1
print(answer)

# 개선된 답안
# 걸린 시간: 엥 근데 이것도 시간 초과(python3) / 9912ms(pypy3)
# 알고리즘: Counter 사용.
import sys
input = sys.stdin.readline
from collections import Counter # (!)

N = int(input().strip())
numbers = [[] for _ in range(4)]
for _ in range(N):
  abcd = list(map(int, input().strip().split()))
  for i in range(4):
    numbers[i].append(abcd[i])

AB = []
for i in range(N):
  for j in range(N):
    AB.append(numbers[0][i] + numbers[1][j])
AB_counter = Counter(AB) # AB 합을 모두 구해서 카운터에 저장

# CD 합을 구하면서 -(c+d)가 AB에 있는지 체크. 없으면 0을 반환.
answer = 0
for i in range(N):
  for j in range(N):
    answer += AB_counter.get(-(numbers[2][i] + numbers[3][j]), 0)

print(answer)
