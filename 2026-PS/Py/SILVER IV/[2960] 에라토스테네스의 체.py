# https://www.acmicpc.net/problem/2960
# 260130 풀이
# 알고리즘: 구현 / 소수 판정 / 에라토스테네스의 체
# 시간: 32ms

# 내 답안
N, K = map(int, input().split())
count = 0
checks = [1] * (N + 1)
flag = False
for number in range(2, N + 1):
    if checks[number] == 0: continue

    now = number
    while now < N + 1:
        if checks[now]:
            checks[now] = 0
            count += 1
            if (count == K): 
                flag = True
                break
        now += number
    if flag: break

print(now)

# 좀 더 파이썬스러운 답안
import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    # 0부터 N까지 체크 배열 (True: 아직 지워지지 않음)
    is_prime = [True] * (n + 1)
    count = 0
    
    for i in range(2, n + 1):
        # i가 이미 지워졌다면 다음 숫자로 (소수가 아닌 경우)
        if not is_prime[i]:
            continue
        # i의 배수들을 i, 2i, 3i ... 순서로 확인
        for j in range(i, n + 1, i):
            if is_prime[j]:
                is_prime[j] = False
                count += 1
                # K번째 지워지는 수라면 출력 후 즉시 종료
                if count == k:
                    print(j)
                    return

if __name__ == "__main__":
    solve()