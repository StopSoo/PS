# https://www.acmicpc.net/problem/3273
# 260120 풀이
# 알고리즘: 정렬(투포인터)
# 시간: 84ms

# 내 답안
# 투포인터 로직을 잘 생각하며서 코드를 짤 것!!!
import sys
input = sys.stdin.readline

n = int(input().strip())
numbers = sorted(list(map(int, input().strip().split())))
x = int(input().strip())

count = 0
i, j = 0, n - 1
while i < j: # 등호는 없어야 함 (!)
    s = numbers[i] + numbers[j]
    if s == x: # 쌍을 찾았을 때도 포인터를 움직여야 함 (!)
        count += 1
        i += 1
        j -= 1
    elif s < x: i += 1
    else: j -= 1
print(count)