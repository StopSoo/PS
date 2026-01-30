# https://www.acmicpc.net/problem/7568
# 260130 풀이
# 알고리즘: 구현 / 브루트포스
# 시간: 36ms

# 내 답안
N = int(input())
values = [list(map(int, input().split())) for _ in range(N)]
answer = []
for i in range(N):
    rank = 1
    for j in range(N):
        if i == j: continue
        if values[i][0] < values[j][0] and values[i][1] < values[j][1]: rank += 1
    answer.append(rank)

print(*answer)

# 리스트 컴프리헨션 사용하기
n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]

ans = [sum(1 for other in p if other[0] > self[0] and other[1] > self[1]) + 1 for self in p]

print(*ans)