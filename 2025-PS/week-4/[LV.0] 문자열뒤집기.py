# https://school.programmers.co.kr/learn/courses/30/lessons/181905

# 내 답안
# list.reverse() -> 리스트를 변경시킴
# reversed(list) -> 변경된 리스트를 반환함
# ''.join(list) -> 리스트 원소들을 공백 없이 붙여 문자열로 반환
def solution(my_string, s, e):
    rList = reversed(list(my_string[s:e+1]))
    answer = my_string[:s] + ''.join(rList) + my_string[e+1:]
    return answer

# 간결한 답안
def solution(my_string, s, e):
    return my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]