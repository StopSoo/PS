# 2752 : 세수정렬
import sys
input = sys.stdin.readline

list_num = list(map(int, input().split()))

list_num.sort()

for i in range(len(list_num)):
    print(list_num[i], end=" ")