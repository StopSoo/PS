# https://school.programmers.co.kr/learn/courses/30/lessons/181878

# 내 답안
# 대소문자 구분X -> 대문자, 소문자 중 한 쪽으로 몰아서 비교 (!)
def solution(myString, pat):
    return int(pat.upper() in myString.upper())