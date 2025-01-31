# https://school.programmers.co.kr/learn/courses/30/lessons/120888

# 내 답안
# but 중복 제거 방법을 참고해서 품
# dict.fromkeys(리스트) -> 리스트 내 중복을 제거 (첫 원소를 남김)
def solution(my_string):
    return ''.join(list(dict.fromkeys(list(my_string))))

def solution(my_string):
    return ''.join(dict.fromkeys(my_string))

# 또 다른 답안
def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer += i
    return answer