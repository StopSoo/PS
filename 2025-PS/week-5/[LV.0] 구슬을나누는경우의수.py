# https://school.programmers.co.kr/learn/courses/30/lessons/120840

# 내 답안
# 처음에는 itertools의 combinations를 사용했는데 시간 초과가 나서 변경!
from math import factorial

def solution(balls, share):
    return factorial(balls) // (factorial(balls-share) * factorial(share))

# 더 간단한 답안
# math에도 comb(조합)이 있다는 걸!
import math

def solution(balls, share):
    return math.comb(balls, share)