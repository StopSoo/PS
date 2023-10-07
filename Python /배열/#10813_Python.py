# 10813 : 공 바꾸기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

array = []
for i in range(N):  # 바구니 채우기
    array.append(i+1)

for _ in range(M):
    i, j = map(int, input().split())    # 바꿀 바구니 번호
    array[i-1], array[j-1] = array[j-1], array[i-1] # swap

# print
for i in range(N):
    print(array[i], end=" ")