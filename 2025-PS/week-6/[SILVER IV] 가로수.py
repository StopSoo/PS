# https://www.acmicpc.net/problem/2485

# 내 답안
from math import gcd
N = int(input())
positions = [int(input()) for _ in range(N)]

gaps = []
answer = 0
for i in range(len(positions)-1): gaps.append(positions[i+1] - positions[i])
gap = gcd(gaps[0], gaps[1]) # 초기화
for i in range(2, len(gaps)): gap = gcd(gap, gaps[i])
for i in range(len(positions)-1): answer += (positions[i+1] - positions[i]) // gap - 1
print(answer)

# 다른 사람의 답안
# gcd에서 인수로 배열을 넣을 때 *를 사용 (!)
import math

def solution(tree):
    n = len(tree)
    distances = [tree[i] - tree[i - 1] for i in range(1, n)]
    gcd_value = math.gcd(*distances)

    result = 0
    for i in distances:
        result += (i // gcd_value) - 1
    return result

N = int(input())
trees = [int(input()) for _ in range(N)]
print(solution(trees))