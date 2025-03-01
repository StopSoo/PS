# https://www.acmicpc.net/problem/26069

# 내 답안
# 걸린 시간: 60ms
# 아래 답안처럼 딕셔너리로 구분하거나, 단순하게는 리스트에 춤추는 사람만 넣는 방법도 있음.
dt = dict()
N = int(input())
for _ in range(N):
  p1, p2 = input().split()
  if p1 == 'ChongChong' or p2 == 'ChongChong':
    dt[p1] = 1
    dt[p2] = 1
  elif p1 in dt.keys() and dt[p1]: dt[p2] = 1
  elif p2 in dt.keys() and dt[p2]: dt[p1] = 1
  else: # 무지개댄스를 추지 않는 사람
    dt[p1] = 0
    dt[p2] = 0

print(list(dt.values()).count(1))