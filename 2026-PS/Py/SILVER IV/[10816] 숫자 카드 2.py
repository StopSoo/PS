# https://www.acmicpc.net/problem/10816
# 260210 풀이
# 알고리즘: 이분 탐색 / 정렬

# 어찌저찌 구현한 답안
# bisect 라이브러리를 복기하자
# 시간: 2284ms
import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

def binary_search(arr, start, end, find_num):
    count = 0
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == find_num:
            left = bisect_left(arr, find_num)
            right = bisect_right(arr, find_num)
            count = right - left
            break
        elif arr[mid] < find_num: start = mid + 1
        else: end = mid - 1
    return count

N = int(input())
numbers = sorted(list(map(int, input().strip().split())))
M = int(input())
check_list = list(map(int, input().strip().split()))

answers = []
for num in check_list:
    answers.append(binary_search(numbers, 0, N - 1, num))
print(*answers)

# 1년 전 내 답안
# 시간: 1088ms
import sys
import bisect

input = sys.stdin.readline
print = sys.stdout.write

def count_by_bisect(arr, target):
    left_index = bisect.bisect_left(arr, target)  # target이 처음 등장하는 위치
    right_index = bisect.bisect_right(arr, target)  # target이 마지막으로 등장한 위치 + 1
    return str(right_index - left_index) + ' '  # 등장한 개수 반환

N = int(input().strip())
cards = sorted(map(int, input().strip().split()))  # 정렬
M = int(input().strip())
numbers = map(int, input().strip().split())

for num in numbers:
    print(count_by_bisect(cards, num))