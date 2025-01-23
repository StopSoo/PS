# https://school.programmers.co.kr/learn/courses/30/lessons/181921

# 내 답안
def solution(l, r):
    answer = []
    number_list = [{"0"}, {"5"}, {"0", "5"}] # 집합들의 리스트
    for num in range(l, r+1):
        if (set(list(str(num))) in number_list):
            answer.append(num)
    if not answer:
        return [-1]
    return answer

# 나랑 비슷하지만 한 번 짚고 넘어갈 만한 답안
# 문자열은 iterable이라 바로 집합화 가능
# return문 한 줄로 작성하기
def solution(l, r):
    answer = []
    for num in range(l, r + 1):
        if not set(str(num)) - set(['0', '5']):
            answer.append(num)
    return answer if answer else [-1]