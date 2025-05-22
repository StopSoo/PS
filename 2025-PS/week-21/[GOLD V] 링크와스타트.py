# https://www.acmicpc.net/problem/15661

# 내 답안
# 걸린 시간: 2452ms(python3) / 1192ms(pypy3)
# 알고리즘: 백트래킹+비트마스킹으로 풀어보려 했는데 브루트포스로 품 ...
# 깨달은 점 1) 뭔가 좀 복잡하면 함수로 빼내자 !!
# 깨달은 점 2) 중복 탐색하는 부분을 어떻게 하면 없앨 수 있을지 고민하자.
import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())
power = list(list(map(int, input().split())) for _ in range(N))
# 두 팀의 능력치 차이를 반환하는 함수
def calculate_gap(start, link):
  point_s, point_l = 0, 0
  for i, j in combinations(start, 2):
    point_s += power[i][j] + power[j][i]
  for i, j in combinations(link, 2):
    point_l += power[i][j] + power[j][i]
  return abs(point_s - point_l)

min_gap = float('inf') # 능력치 차이의 최솟값
for count in range(1, N):
  for start in combinations(range(1, N), count - 1): # 팀 고르기 (0번 사람을 start 팀에 넣어서 중복 탐색 제거)
    start_team = (0, ) + start # 0번 포함 
    link_team = [i for i in range(N) if i not in start_team]
    
    gap = calculate_gap(start_team, link_team)
    if gap == 0: # 0이 나올 수 있는 값들 중 최솟값이므로 바로 종료
      print(0)
      sys.exit(0)
    min_gap = min(min_gap, gap) # 0이 아니라면 업데이트

print(min_gap)

# 백트래킹 + 비트마스킹으로 푼다면?
# 근데 이해는 안됨 ... 
import sys
input = sys.stdin.readline

N = int(input())
power = [list(map(int, input().split())) for _ in range(N)]

min_gap = float('inf')

def calculate_gap(bitmask):
  start = []
  link = []
  for i in range(N):
    if bitmask & (1 << i): start.append(i)
    else: link.append(i)

  point_s, point_l = 0, 0
  for i in range(len(start)):
    for j in range(i+1, len(start)):
      point_s += power[start[i]][start[j]] + power[start[j]][start[i]]
  for i in range(len(link)):
    for j in range(i+1, len(link)):
      point_l += power[link[i]][link[j]] + power[link[j]][link[i]]
  return abs(point_s - point_l)

def backtrack(idx, bitmask, count):
  global min_gap
  # 한 팀이 비었으면 안 됨, 두 팀으로 나누려면 count는 1 이상 1명 이상은 제외해야 함
  if idx == N:
    if 0 < count < N:
      gap = calculate_gap(bitmask)
      if gap == 0:
        print(0)
        sys.exit(0)
      min_gap = min(min_gap, gap)
    return
  # idx 번째 사람을 start 팀에 넣음
  backtrack(idx + 1, bitmask | (1 << idx), count + 1)
  # idx 번째 사람을 link 팀에 넣음
  backtrack(idx + 1, bitmask, count)

backtrack(0, 0, 0)
print(min_gap)