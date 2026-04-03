# https://school.programmers.co.kr/learn/courses/30/lessons/120956
# 260403 풀이

# 내 답안
# replace 결과로 변경하려면 꼭 재할당을 해줘야 한다.
def solution(babbling):
    answer = 0
    pos = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        for p in pos:
            if p in word: word = word.replace(p, ' ')
        if word.strip() == '': answer += 1
    
    return answer

# 다른 사람의 답안 (정규식 사용)
import re

def func(babbling):
    regex = re.compile('^(aya|ye|woo|ma)+$') # 문제의 조건에 완벽히 부합하는 정규식은 아님 .. 하지만 주어진 입력값 제한 사항에 대해서는 통과됨
    cnt = 0
    for e in babbling:
        if regex.match(e):
            cnt += 1
    return cnt