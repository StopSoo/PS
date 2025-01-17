# https://school.programmers.co.kr/learn/courses/30/lessons/181914

# 내 답안
def solution(number):
    answer = 0
    for num in number:
        answer += int(num)
    return answer % 9

# 간결한 답안
def solution(number):
    return sum(list(map(int, number))) % 9