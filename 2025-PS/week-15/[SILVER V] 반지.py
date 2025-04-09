# https://www.acmicpc.net/problem/5555

# 내 답안
# 걸린 시간: 36ms
# 처음에는 deque 방식을 이용했지만, 확실한 방법인 "문자열 이어붙이기"를 이용하는 게 나음 (!)
find_word = input()
N = int(input())
count = 0
for _ in range(N):
  ring = input()
  doubled_ring = ring + ring
  if find_word in doubled_ring:
    count += 1
print(count)