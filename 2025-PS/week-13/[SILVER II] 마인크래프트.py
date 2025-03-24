# https://www.acmicpc.net/problem/18111

# 내 답안
# 하지만 시간 초과 (!) 끝까지 해결 못 함 ...
# 문제를 꼼꼼히 읽자 !!
import sys
input = sys.stdin.readline

N, M, B = map(int, input().strip().split())
blocks = [list(map(int, input().strip().split())) for _ in range(N)]
max_b, min_b = 0, float('inf')
for i in range(N):
  for j in range(M):
    if blocks[i][j] > max_b: max_b = blocks[i][j]
    if blocks[i][j] < min_b: min_b = blocks[i][j]

answer = float('inf') # 시간
answer_h = 0 # 높이
for h in range(max_b, min_b-1, -1):
  temp_B = B
  count_remove = sum([blocks[i][j] - h for i in range(N) for j in range(M) if blocks[i][j] > h])
  temp_B += count_remove # 제거한 블록을 인벤토리에 추가
  count_add = sum([h - blocks[i][j] for i in range(N) for j in range(M) if blocks[i][j] < h])
  if count_add > temp_B: continue
  if answer > count_remove*2 + count_add:
    answer = count_remove*2 + count_add
    answer_h = h

print(answer, answer_h)

# 시간 초과를 개선한 답안
# 걸린 시간: 196ms
# 위 코드에서 count_remove/count_add 구할 때 매번 O(NM)의 시간 복잡도로 구했던 것을 딕셔너리를 통해 개선 (!)
import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(N)]

height_counts = {} # 높이별 블록 개수 저장
min_h, max_h = 256, 0 # 최대/최소 높이 저장

for i in range(N):
  for j in range(M):
    h = blocks[i][j]
    height_counts[h] = height_counts.get(h, 0) + 1
    min_h = min(min_h, h)
    max_h = max(max_h, h)

answer_time = float('inf')
answer_h = 0
for h in range(max_h, min_h - 1, -1): # 가능한 모든 높이 탐색
  count_remove = 0  # 제거할 블록 개수
  count_add = 0  # 추가할 블록 개수

  for height, count in height_counts.items():
    if height > h:
      count_remove += (height - h) * count  # 블록을 제거해야 함
    elif height < h:
      count_add += (h - height) * count  # 블록을 추가해야 함
  # 인벤토리에 있는 블록이 충분한 경우에만 진행
  if count_remove + B >= count_add:
    total_time = count_remove * 2 + count_add
    # 최소 시간 갱신, 같은 경우 더 높은 높이 선택
    if total_time < answer_time or (total_time == answer_time and h > answer_h):
      answer_time = total_time
      answer_h = h

print(answer_time, answer_h)

