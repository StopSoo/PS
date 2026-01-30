# https://www.acmicpc.net/problem/1018
# 260130 풀이
# 알고리즘: 구현 / 브루트포스
# 시간: 68ms

N, M = map(int, input().split())
chess = list(input() for _ in range(N))

ans1 = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']
ans2 = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']

answers = []
for i in range(N - 7): # 행 시작 인덱스
    for j in range(M - 7): # 열 시작 인덱스
        cnt1, cnt2 = 0, 0
        for idx_r, row in enumerate(chess[i:i+8]):
            for idx_c, ele in enumerate(row[j:j+8]):
                if ele != ans1[idx_r][idx_c]: cnt1 += 1
                if ele != ans2[idx_r][idx_c]: cnt2 += 1
        answers.append(min(cnt1, cnt2))

print(min(answers))