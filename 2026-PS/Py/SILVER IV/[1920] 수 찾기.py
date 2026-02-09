# https://www.acmicpc.net/problem/1920
# 260209 풀이
# 알고리즘: 정렬 / 이분 탐색

# 내 답안
# 시간: 584ms
def binary_search(arr, start, end, find_num):
    if start > end or arr[start] > find_num or arr[end] < find_num: return 0

    mid = (start + end) // 2
    if arr[mid] == find_num: return 1
    elif arr[mid] < find_num: return binary_search(arr, mid + 1, end, find_num)
    else: return binary_search(arr, start, mid - 1, find_num)

import sys
input = sys.stdin.readline

N = int(input().strip())
numbers = sorted(list(map(int, input().strip().split()))) # 무조건 정렬!
M = int(input().strip())
find = list(map(int, input().strip().split()))

for i in range(M):
    print(binary_search(numbers, 0, N-1, find[i]))

# 내 답안을 개선한 코드
# 시간: 412ms
import sys
input = sys.stdin.readline

def binary_search(arr, start, end, find_num):
    # 재귀 대신 반복문을 사용하여 효율성 극대화
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == find_num: return 1
        elif arr[mid] < find_num: start = mid + 1
        else: end = mid - 1
    return 0 # 값을 찾지 못하고 반복문이 종료된 경우

N = int(input().strip())
numbers = sorted(list(map(int, input().split())))
M = int(input().strip())
find = list(map(int, input().split()))

for i in range(M):
    sys.stdout.write(str(binary_search(numbers, 0, N-1, find[i])) + '\n')

# 집합을 이용해 풀었던 내 답안
# 근데 이건 파이썬이라 통과한 듯, 이분 탐색도 안 사용함 
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().strip())
set1 = set(map(int, input().strip().split()))
M = int(input().strip())
set2 = list(map(int, input().strip().split()))

for number in set2:
    if number in set1: print('1\n')
    else: print('0\n')