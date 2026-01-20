# https://www.acmicpc.net/problem/11004
# 260120 풀이
# 알고리즘: 정렬(퀵 정렬)
# 시간:

# 답안 1
# 그냥 파이썬 내장 정렬 함수로 풀기 -> 실전 코테에서 사용하기 !!!!!
# 시간: 2736ms
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

print(A[K-1])

# 답안 2
# 퀵 정렬로 배열 전체를 정렬하기에는 너무 느림. 따라서 "퀵 선택 정렬"을 사용하자!
# 시간: 2248ms
import sys
import random

def quick_select(arr, k):
    if len(arr) == 1:
        return arr[0]
    # 피벗을 랜덤하게 선택하기
    pivot = random.choice(arr)
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    # k번째가 어느 그룹에 속하는지 확인하고 해당 그룹만 탐색
    if k <= len(left):
        return quick_select(left, k)
    elif k <= len(left) + len(middle):
        return pivot
    else:
        return quick_select(right, k - len(left) - len(middle))

sys.setrecursionlimit(10**6)

import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
A = list(map(int, input().strip().split()))
print(quick_select(A, K))