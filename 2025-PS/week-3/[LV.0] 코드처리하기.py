# https://school.programmers.co.kr/learn/courses/30/lessons/181932

# 내 답안
def solution(code):
    mode = 0
    answer = ''
    for i in range(len(code)):
        if code[i] == "1":
            mode = (mode + 1) % 2
        elif mode == 0 and i % 2 == 0:
            answer += code[i]
        elif mode == 1 and i % 2 != 0:
            answer += code[i]
    
    return answer if answer else "EMPTY"

# 숏코딩
def solution(code):
    return "".join(code.split("1"))[::2] or "EMPTY"