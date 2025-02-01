# https://school.programmers.co.kr/learn/courses/30/lessons/181862

# 내 답안
def solution(myStr):
    answer = ''
    for word in list(myStr):
        if word == 'a' or word == 'b' or word == 'c': answer += ' '
        else: answer += word
    return answer.split() if answer.split() != [] else ["EMPTY"]

# 비슷하지만 좀 더 간결한 답안
def solution(myStr):
    answer = [x for x in myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split() if x]
    return answer if answer else ['EMPTY']