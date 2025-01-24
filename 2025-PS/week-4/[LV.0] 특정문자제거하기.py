# https://school.programmers.co.kr/learn/courses/30/lessons/120826

# 내 답안
# index가 없을 경우 ValueError를 반환하므로 try-except문 사용
def solution(my_string, letter):
    answer = list(my_string)
    
    try:
        while True:
            ind = answer.index(letter)
            del answer[ind]
    except:
        return ''.join(answer)

# 간결한 답안
# replace를 적재적소에 활용하자
def solution(my_string, letter):
    return my_string.replace(letter, '')