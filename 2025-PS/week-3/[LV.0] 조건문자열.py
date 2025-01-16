# https://school.programmers.co.kr/learn/courses/30/lessons/181934

# 내 답안
def solution(ineq, eq, n, m):
    answer = 0
    if ineq + eq == ">=":
        answer = n >= m
    elif ineq + eq == "<=":
        answer = n <= m
    elif ineq + eq == ">!":
        answer = n > m
    else:
        answer = n < m
    
    if answer == True:
        return 1
    else:
        return 0

# 간결한 답안
# eval() 사용
def solution(ineq, eq, n, m):
    return int(eval(str(n) + ineq + eq.replace('!', '') + str(m)))

# 또 다른 답안
# false 설정해두고 바뀌는 경우만 체크
def solution(ineq, eq, n, m):
    answer = 0
    if n > m and ineq ==">":
        answer = 1
    elif n < m and ineq == "<":
        answer = 1
    elif n == m and eq == "=":
        answer = 1

    return answer