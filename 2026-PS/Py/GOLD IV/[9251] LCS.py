# https://www.acmicpc.net/problem/9251
# 260121 풀이
# 알고리즘: 최장 공통 부분 수열
# 시간: 408ms

S1 = input()
S2 = input()
l1, l2 = len(S1), len(S2)
S1, S2 = " " + S1, " " + S2 # 1 기반 인덱스

arr = [[0] * (l2 + 1) for _ in range(l1 + 1)]
for i in range(1, l1 + 1):
    for j in range(1, l2 + 1):
        if S1[i] == S2[j]:
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])
print(arr[l1][l2])