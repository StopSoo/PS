# https://www.acmicpc.net/problem/1966
# 260129 풀이
# 알고리즘: 구현 / 시뮬레이션

# 내 답안 1
from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    queue = deque([(num, i == M) for i, num in enumerate(numbers)])

    count = 1 # 현재 순서
    while True:
        if queue[0][1] and queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            print(count)
            break
        elif queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            queue.popleft()
        else:
            queue.rotate(-1)

# 내 답안 2
# 시간: 36ms
import sys
input = sys.stdin.readline

def print_order(N, M, numbers):
    queue = [(i, p) for i, p in enumerate(numbers)]
    order = 0

    while queue:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue): queue.append(cur)
        else:
            order += 1
            if cur[0] == M: return order

T = int(input().strip())
for _ in range(T):
    N, M = map(int, input().strip().split())
    numbers = list(map(int, input().strip().split()))
    print(print_order(N, M, numbers))