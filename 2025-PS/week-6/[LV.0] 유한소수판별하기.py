# https://school.programmers.co.kr/learn/courses/30/lessons/120878#

# 내 답안
def solution(a, b):
    for d in range(2, a+1): # 기약분수
        while a%d == 0 and b%d == 0: a, b = a//d, b//d
    if b == 1: return 1 # 정수

    factors = [] # 소인수
    for d in range(2, b+1):
        while b%d == 0: 
            factors.append(d)
            b //= d
    conditions = [[2], [5], [2, 5]]
    return 1 if list(set(factors)) in conditions else 2

# 유클리드 호제법을 활용한 깔끔한 답안
# gcd(): 최대공약수
from math import gcd
def solution(a, b):
    b //= gcd(a,b)
    while b%2 == 0:
        b //= 2
    while b%5 == 0:
        b //= 5
    return 1 if b == 1 else 2