# https://school.programmers.co.kr/learn/courses/30/lessons/120875
# 260403 풀이

# 내 답안
# 점이 4개로 고정된 게 아니라면 combinations 사용하기 ~
def solution(dots):
    orders = [[0, 1, 2, 3], [0, 2, 1, 3], [0, 3, 1, 2]]
    for t1_1, t1_2, t2_1, t2_2 in orders:
        val1 = (dots[t1_1][1] - dots[t1_2][1]) / (dots[t1_1][0] - dots[t1_2][0])
        val2 = (dots[t2_1][1] - dots[t2_2][1]) / (dots[t2_1][0] - dots[t2_2][0])
        if val1 == val2: return 1
    return 0
