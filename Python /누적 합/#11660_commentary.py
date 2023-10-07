# 11660_commentary

import sys
input = sys.stdin.readline

n, m = map(int, input().split())        # map 함수를 이용해서 형 변환
A = [[0] * (n+1)]
D = [[0] * (n+1) for _ in range(n+1)]

for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)     # 행 추가

# 합 배열을 구하는 과정
for i in range(n+1):
    D[i][1] = D[i-1][1] + A[i][1]
    D[1][i] = D[1][i-1] + A[1][i]

for i in range(2, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

# 질의 x1, y1, x2, y2에 대한 답을 구간 합으로 구하는 방법
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)