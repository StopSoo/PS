# https://school.programmers.co.kr/learn/courses/30/lessons/12903?language=python3

# 내 답안
def solution(s):
    if len(s) % 2 == 1: return s[len(s) // 2]
    else: return s[len(s)//2-1:len(s)//2+1]

# 한 줄 답안
# 문자열 길이의 짝/홀 여부를 모두 적용한 코드
def string_middle(str):
    return str[(len(str)-1)//2 : len(str)//2 + 1]