# https://www.acmicpc.net/problem/1931

# 내 답안
# 걸린 시간: 368ms
# 그리디 알고리즘 -> 끝나는 시간이 빠를수록 좋은 것 (!)
# 그게 최선의 선택이라고 믿기 때문에 시작 회의의 경우에 따라 비교할 필요가 없는 것. (내가 가장 헷갈린 부분)
import sys
input = sys.stdin.readline

N = int(input().strip())
times = [list(map(int, input().strip().split())) for _ in range(N)]
times = sorted(times, key=lambda x: [x[1], x[0]])

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