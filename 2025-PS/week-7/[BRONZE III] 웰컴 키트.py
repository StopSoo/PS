# https://www.acmicpc.net/problem/30802

# 내 답안
from math import ceil

N = int(input()) # 참가자의 수
people = list(map(int, input().split())) # 사이즈 별 신청자의 수
T, P = map(int, input().split()) # 티셔츠, 펜의 묶음 수 

count_shirt = sum([ceil(p / T) for p in people])
count_pencil, pencil = N // P, N % P

print(count_shirt)
print(count_pencil, pencil)