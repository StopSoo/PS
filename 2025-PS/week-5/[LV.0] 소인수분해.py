# https://school.programmers.co.kr/learn/courses/30/lessons/120852

# 내 답안
# 소수를 따로 추려낼 필요는 X. while문으로 다 나눠질 때까지 나눈 후 다음 수로 넘어가니까!
def solution(n):
    factors = []
    for d in range(2, n+1) :
        while n % d == 0:
            factors.append(d)
            n = n // d

    return sorted(list(set(factors)))