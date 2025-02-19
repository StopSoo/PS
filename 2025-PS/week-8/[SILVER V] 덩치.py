# https://www.acmicpc.net/problem/7568

# 내 답안
# 걸린 시간: 40ms
# "N명의 집단에서 각 사람의 덩치 등수는 자신보다 더 "큰 덩치"의 사람의 수로 정해진다."
# 처음 코드에서는 일반 랭킹 기준으로 해서 틀렸음. 문제를 잘 읽자 !!
N = int(input())
values = [list(map(int, input().split())) for _ in range(N)] # 몸무게 키
counts = []
for i, [w1, h1] in enumerate(values): # 체크하려는 사람
  count = 0 # 나보다 덩치가 큰 사람의 수
  for j, [w2, h2] in enumerate(values): # 비교 대상
    if i == j: continue
    if w1 < w2 and h1 < h2: count += 1
  counts.append(count)
ranks = [x + 1 for x in counts]
print(*ranks)