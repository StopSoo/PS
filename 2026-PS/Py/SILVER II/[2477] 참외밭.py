# https://www.acmicpc.net/problem/2477
# 260203 풀이
# 알고리즘: 구현 / 수학 / 기하학

# 내 답안
# 시간: 36ms
# 기본적인 아이디어는 알겠으나, 구현 방식을 모르겠어서 질문함
# <포인트> 큰 직사각형의 가로, 세로 길이 원소에서 인덱스 3개 차이 나는 원소가 작은 직사각형의 가로, 세로 길이 원소이다. (!)
# 하지만 ... 내 코드 너무 지저분함
K = int(input())
infos = [list(map(int, input().split())) for _ in range(6)]
# 큰 직사각형의 가로, 세로 길이, 각 인덱스
l1 = max(l for d, l in infos if d == 1 or d == 2)
l2 = max(l for d, l in infos if d == 3 or d == 4)
ind1 = [i for i, (d, l) in enumerate(infos) if (d == 1 or d == 2) and l == l1][0]
ind2 = [i for i, (d, l) in enumerate(infos) if (d == 3 or d == 4) and l == l2][0]

answer = l1 * l2 - infos[(ind1 + 3) % 6][1] * infos[(ind2 + 3) % 6][1]
print(answer * K)

# 개선된 코드
# 시간: 32ms
import sys
input = sys.stdin.readline

K = int(input())
infos = [list(map(int, input().split())) for _ in range(6)]
# 1. 가로(1, 2) 중 최대, 세로(3, 4) 중 최대 인덱스 찾기
max_w_idx = 0
max_h_idx = 0
max_w = 0
max_h = 0

for i in range(6):
    d, l = infos[i]
    if d == 1 or d == 2: # 가로 방향
        if l > max_w:
            max_w = l
            max_w_idx = i
    else: # 세로 방향
        if l > max_h:
            max_h = l
            max_h_idx = i
# 2. 큰 사각형 넓이
big_area = max_w * max_h
# 3. 작은 사각형 넓이 (가장 긴 변 인덱스에서 3번째 떨어진 변들)
small_area = infos[(max_w_idx + 3) % 6][1] * infos[(max_h_idx + 3) % 6][1]
print((big_area - small_area) * K)