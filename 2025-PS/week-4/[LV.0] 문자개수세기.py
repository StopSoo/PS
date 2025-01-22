# https://school.programmers.co.kr/learn/courses/30/lessons/181902

# 내 답안
# ord
# 알파벳 대소문자 구분 -> isupper(), islower() 사용도 체크
def solution(my_string):
    answer = [0] * 52 # 초기화
    for c in my_string:
        if ord(c) < 97: 
            answer[ord(c)-65] += 1
        else:
            answer[ord(c)-71] += 1
    return answer