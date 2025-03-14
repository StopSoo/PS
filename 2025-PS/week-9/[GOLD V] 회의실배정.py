# https://www.acmicpc.net/problem/1931

# 내 답안
# 걸린 시간: 368ms
# 그리디 알고리즘 -> 끝나는 시간이 빠를수록 좋은 것 (!) -> 끝점을 기준으로 정렬 후, 끝점이 작은 거 위주로 선택.
# 그게 최선의 선택이라고 믿기 때문에 시작 회의의 경우에 따라 비교할 필요가 없는 것. (내가 가장 헷갈린 부분)
# "정렬 + 그리디"는 자주 쓰이는 조합 !! 
import sys
input = sys.stdin.readline

N = int(input().strip())
times = [list(map(int, input().strip().split())) for _ in range(N)]
times = sorted(times, key=lambda x: [x[1], x[0]]) # 끝점을 기준으로 오름차순 정렬 (x[0]도 꼭 넣어줘야 함 !!)

now, nx = 0, 1
count = 1
while nx < N:
  start = times[nx][0]
  end = times[now][1]
  if end > start:
    nx += 1 # 다음 시간으로 이동
  else:
    now = nx
    nx = now + 1
    count += 1
print(count)

# "좌표 압축 + DP"를 활용한 코드
import sys
input = sys.stdin.readline

N = int(input())
nums = []
times = []

for _ in range(N):
  s, e = map(int, input().split())
  times.append((s, e))
  nums.append(s) # 좌표 압축을 위한 추가
  nums.append(e)
# 좌표 압축
nums = sorted(list(set(nums)))
T = len(nums)

convert = dict()
for idx, num in enumerate(nums, 1):
  convert[num] = idx
# 풀이
# starts[t] = 끝나는 시각이 t인 회의들의 시작 시간들을 담은 리스트
starts = dict() 
for i in range(N):
  tmp0, tmp1 = convert[times[i][0]], convert[times[i][1]]
  if tmp1 in starts:
    starts[tmp1].append(tmp0)
  else:
    starts[tmp1] = [tmp0]

for key in starts: starts[key].sort() # 시작 시간이 빠른 순대로 정렬하기 위함

dp = [0] * (T+1) # 좌표 압축 시 1이 가장 작은 수였으므로, 0이라는 시간은 나올 수 X
for t in range(1, T+1): # dp[t]
  dp[t] = dp[t-1]
  if t in starts:
    for s in starts[t]:
      dp[t] = max(dp[t], dp[s] + 1)

print(dp[T])