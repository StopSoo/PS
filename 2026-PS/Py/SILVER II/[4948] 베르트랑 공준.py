# https://www.acmicpc.net/problem/4948
# 260106 풀이
# 알고리즘: 소수 판정, 에라토스테네스의 체
# 시간: 해결 못 함 !!!!!!

import sys, math
input = sys.stdin.readline

numbers = []
while True:
    n = int(input())
    if n != 0: numbers.append(n)
    else: break

# 에라토스테네스의 체
max_number = max(numbers)
check = [1] * (max_number * 2 + 1)

for num in range(max_number * 2 + 1):
    if num == 0 or num == 1: 
        check[num] = 0
        continue

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            check[num] = 0
            continue

# 입력 받은 숫자별 범위 내 소수 개수 구하기
for num in numbers:
    print(check[num + 1:num*2 + 1].count(1))

# 정답 코드 
# 시간: 124ms (!!!)
import sys, math
input = sys.stdin.readline

LIMIT = 123456 * 2 # 이미 정해진 한계를 이용하기
check = [1] * (LIMIT + 1)
check[0] = check[1] = 0
# 에라토스테네스의 체
for i in range(2, int(math.sqrt(LIMIT)) + 1):
    if check[i]: # 배수 지우기 (!)
        for j in range(i * i, LIMIT + 1, i):
            check[j] = 0
# 결과 출력
while True:
    n = int(input())
    if n == 0: break

    print(sum(check[n + 1 : n * 2 + 1]))