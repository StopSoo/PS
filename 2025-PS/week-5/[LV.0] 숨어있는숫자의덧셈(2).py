# https://school.programmers.co.kr/learn/courses/30/lessons/120864

# 내 답안
def solution(my_string):
    result = 0
    str_number = ''
    for x in my_string:
        if x.isdigit(): 
            str_number += x
        else:
            if str_number: # 조건 꼭 추가
                result += int(str_number)
            str_number = ''
    if str_number: result += int(str_number) # 숫자로 끝나는 경우도 체크
    return result

# 간결하고 정확한 답안
# 숫자가 아닐 때는 공백을 추가하고, 공백으로 분리 후 합을 계산 (!)
def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())