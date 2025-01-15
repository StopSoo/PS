# 항상 brute-force가 가능한지부터 확인하기
# 그리디 알고리즘 - 한 번에 M권을 들기 / 방향 바꾸지 않기 / 먼 곳을 먼저 가기 (!)

N, M = map(int, input().split()) # 책의 총 개수, 한 번에 들 수 있는 책의 개수
positions = list(map(int, input().split()))

neg = [] # 음수 좌표
pos = [] # 양수 좌표
for x in positions:
  if x > 0:
    pos.append(x)
  else:
    neg.append(-x) # 거리이므로 음수 처리

pos = sorted(pos)[::-1]
neg = sorted(neg)[::-1]

dists = []
# M개 단위로 끊기
for p in pos[::M]:
  dists.append(p)

for n in neg[::M]:
  dists.append(n)

ans = 2 * sum(dists) - max(dists) # 가장 먼 거리는 한 번만 감
print(ans)