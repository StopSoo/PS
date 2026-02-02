# https://www.acmicpc.net/problem/8979
# 260202 풀이
# 알고리즘: 구현 / 정렬

# 내 답안
# 시간: 324ms (100점)
# 반복문 로직 자체가 너무 복잡하고 헷갈리기 쉬움
# 게다가 N번을 다 훑는 거라 비효율적임
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
scores = []
ranks = [0] * N
for _ in range(N):
    infos = list(map(int, input().split()))
    scores.append(infos[1:] + [infos[0]])

scores = sorted(scores, key=lambda x: x[3])

for i in range(N):
    rank = 1
    g_i, s_i, d_i = scores[i][:3]
    for j in range(N):
        g_j, s_j, d_j = scores[j][:3]
        if g_i < g_j:
            rank += 1
        elif g_i == g_j:
            if s_i < s_j:
                rank += 1
            elif s_i == s_j:
                if d_i < d_j:
                    rank += 1
    ranks[i] = rank

print(ranks[K - 1])

# 개선된 답안
# 시간: 36ms 
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
medals = []

for _ in range(N):
    temp = list(map(int, input().split()))
    medals.append(temp)
# 금(1), 은(2), 동(3) 메달 순으로 내림차순 정렬
medals.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)
# K번 국가가 몇 번째 인덱스에 있는지 찾기
target_idx = 0
for i in range(N):
    if medals[i][0] == K:
        target_idx = i
        break
# K번 국가와 메달 기록이 똑같은 '가장 앞선 국가'의 인덱스가 곧 등수
for i in range(N):
    if medals[i][1:4] == medals[target_idx][1:4]:
        print(i + 1)
        break