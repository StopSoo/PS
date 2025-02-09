# https://www.acmicpc.net/problem/2485

# 내 답안
from math import gcd
N = int(input())
positions = [int(input()) for _ in range(N)]

gaps = []
for i in range(len(positions)-1): gaps.append(positions[i+1] - positions[i])
gap = gcd(gaps[0], gaps[1])