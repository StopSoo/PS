# https://www.acmicpc.net/problem/10810

# 내 답안
# 걸린 시간: 36ms
# "시뮬레이션"이라고 해서 특별한 알고리즘이 있는 것은 아니고, 입력 조건을 순서대로, 정확하게 따라가는 과정이 중요하다(!)
N, M = map(int, input().split())
baskets = [0] * (N + 1)

for _ in range(M):
  s, e, k = map(int, input().split())
  for idx in range(s, e + 1):
    baskets[idx] = k
print(*baskets[1:])