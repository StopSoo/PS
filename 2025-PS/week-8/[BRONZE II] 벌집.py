# https://www.acmicpc.net/problem/2292

# 내 답안
# 걸린 시간: 40ms
N = int(input())

answer = 1 # 정답
layer, total = 1, 1 # 층 수, 누적 방 번호
while True:
  if N == 1:
    break
  if N <= total + layer * 6:
    answer += layer
    break
  else:
    total += layer * 6
    layer += 1
print(answer)