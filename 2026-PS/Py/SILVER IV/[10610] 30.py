# https://www.acmicpc.net/problem/10610
# 260203 풀이
# 알고리즘: 정렬
# 시간: 56ms

# 내 답안
# 헷갈렸던 점 1) sort() 함수 쓸 때 reverse 조건 -> reversed인 줄 알았음
# 헷갈렸던 점 2) join() 함수 쓸 때 자바스크립트랑 헷갈림
import sys
input = sys.stdin.readline

N = list(input().strip())
if '0' not in N:
    print(-1)
else:
    if sum(int(n) for n in N) % 3 == 0:
        N.sort(reverse=True)
        print(''.join(N))
    else: print(-1)