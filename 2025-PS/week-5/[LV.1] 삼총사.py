# https://school.programmers.co.kr/learn/courses/30/lessons/131705?language=python3

# 내 답안
# 조합(combinations)을 사용
from itertools import combinations

def solution(number):
    answer = 0
    for comb in combinations(number, 3):
        if sum(comb) == 0: answer += 1
    return answer
