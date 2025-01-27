# https://school.programmers.co.kr/learn/courses/30/lessons/181847

# 내 답안
def solution(n_str):
    ind = 0
    for i in range(len(n_str)):
        if n_str[i] == '0': ind += 1
        else: break
    return n_str[ind:]

# 알아두어야 할 함수
# lstrip: left-strip
def solution(n_str):
    return n_str.lstrip('0')