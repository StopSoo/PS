# 10810 : 공 넣기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

array = [0] * N     # 바구니 배열 -> 0으로 초기화 
for _ in range(M):
    i, j, k = map(int, input().split()) # i번부터 j번 바구니까지 k공을 넣는다.
    for a in range(i-1, j):
        array[a] = k

# print
for i in range(N):
    print(array[i], end=" ")