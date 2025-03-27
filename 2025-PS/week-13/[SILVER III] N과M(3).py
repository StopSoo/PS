# https://www.acmicpc.net/problem/15651

# 내 답안
# 걸린 시간: 1856ms
# 중복 순열(product) 이용하기 (!)
from itertools import product

N, M = map(int, input().split())
for p in product(range(1, N+1), repeat=M):
  print(*p)

# 백트래킹을 이용한 코드
# 걸린 시간: 1864ms
N, M = map(int, input().split())
ans = []

def back():
  if len(ans) == M:
    print(*ans)
    return
  for i in range(1, N+1): # 중복 허용
    ans.append(i)
    back()
    ans.pop()

back()