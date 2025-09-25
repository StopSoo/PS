# https://www.acmicpc.net/problem/3078

# 내 답안
# 걸린 시간: 248ms
# 알고리즘: 슬라이딩 윈도우 / 투포인터 -> N이 최대 30만이므로 포인터를 조건에 맞게 잘 옮겨야 시간초과가 안 난다.

# 좋은 친구의 조건
# 1. 등수의 차이가 K 이하이다.
# 2. 이름의 길이가 같다.
import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
students = []
for i in range(N):
  name = input().strip()
  students.append(len(name)) # 이름 길이만 저장

count = 0
length_count = [0] * 21 # 이름 길이별 학생 수(2 ~ 20)
i = 0

for j in range(N):
  # 지금까지 이름이 같은 길이인 학생 수
  count += length_count[students[j]]
  length_count[students[j]] += 1
  # 범위가 K를 넘어가면 i 이동 (투포인터를 사용할 거면 이렇게 사용해라!)
  if j - i >= K:
    length_count[students[i]] -= 1
    i += 1

print(count)

# 슬라이딩윈도우 + 큐(deque)를 사용한 방법(이게 더 정석!!)
# 이름 길이별로 학생 수를 세어두면, 현재 학생의 이름 길이와 같은 길이를 가진 학생 수만큼 쌍 개수를 구할 수 있다.
# deque를 길이별로 유지하고, 길이에 대해 등수를 저장.
# deque에서 idx 차이가 K보다 큰 학생들은 빼준다. deque에서 남아있는 애들은 지금 학생과 좋은 친구 쌍이 될 수 있음.
# 걸린 시간: 320ms
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
# 이름 길이별 큐 
queues = [deque() for _ in range(21)]
count = 0

for i in range(N):
  name = input().strip()
  l = len(name)
  # 현재 학생보다 K 이상 차이 나는 학생은 제거
  while queues[l] and i - queues[l][0] > K:
    queues[l].popleft()
  # 지금 큐에 남아있는 학생들은 모두 좋은 친구
  count += len(queues[l])
  # 현재 학생 추가
  queues[l].append(i)

print(count)