# https://www.acmicpc.net/problem/4673
# 260128 풀이
# 알고리즘: 구현 / 브루트포스
# 시간: 272ms

check = [0] * 10001
for num in range(1, 10001):
    if check[num]: continue
    now = num
    while now < 10000:
        now = now + sum(map(int, list(str(now))))
        if now < 10001: 
            check[now] = 1

answer = [num for num in range(1, 10001) if not check[num]]
print(*answer, sep='\n')