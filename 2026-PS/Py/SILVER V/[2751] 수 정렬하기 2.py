# https://www.acmicpc.net/problem/2751
# 260120 풀이

# 2025년 2월의 답안 참고해서 작성한 코드
# 빠른 입출력 사용
# 알고리즘: 정렬(일반 정렬)
# 시간: 896ms
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().strip())
numbers = sorted([int(input().strip()) for _ in range(N)])
for num in numbers: print(str(num) + '\n')

# 2026년 1월의 답안
# N이 최대 100만이므로 일반 정렬로는 풀 수 없음.
# 알고리즘: 정렬(병합 정렬)
# 시간: 3460ms
def merge_sort(arr):
    if len(arr) <= 1: return arr
    # Divide
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    # Conquer
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    # Combine
    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result += left[i:]
    result += right[j:]
    return result

import sys
input = sys.stdin.readline

N = int(input().strip())
numbers = [int(input().strip()) for _ in range(N)]
for number in merge_sort(numbers): # 정렬 함수를 반드시 호출해야 함 !!!
    print(number)