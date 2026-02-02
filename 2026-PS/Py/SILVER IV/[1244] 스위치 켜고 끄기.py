# https://www.acmicpc.net/problem/1244
# 260202 풀이
# 알고리즘: 구현 / 시뮬레이션
# 시간: 32ms

# 내 답안
# 시간 초과 이유 1. 출력 조건을 잘 확인하자 !!!! -> 20개씩 끊어 출력
# 시간 초과 이유 2. while문 내부에 break 조건 누락
import sys
input = sys.stdin.readline

S = int(input()) # 스위치 개수
switches = list(map(int, input().split()))
s_count = int(input())
students = list(list(map(int, input().split())) for _ in range(s_count))

for sex, number in students:
    if sex == 1: # 남학생
        for i in range(number, S + 1, number):
            switches[i - 1] = 1 - switches[i - 1]
    else: # 여학생
        i, j = number - 2, number
        switches[number - 1] = 1 - switches[number - 1]
        while True:
            if i < 0 or j == S: break
            if switches[i] == switches[j]:
                switches[i] = 1 - switches[i]
                switches[j] = 1 - switches[j]
                i, j = i - 1, j + 1
            else: break

for i in range(0, S, 20):
    print(*switches[i:i + 20])