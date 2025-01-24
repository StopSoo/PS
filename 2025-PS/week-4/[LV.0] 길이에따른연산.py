# https://school.programmers.co.kr/learn/courses/30/lessons/181879

# 내 답안
def solution(num_list):
    answer = 1
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        for i in range(len(num_list)):
            answer *= num_list[i]
        return answer

# 알아두어야 할 함수
# sum(리스트): 리스트 내 원소들의 합을 반환 / prod(리스트): 리스트 내 원소들의 곱을 반환
from math import prod
def solution(num_list):
    return sum(num_list) if len(num_list) >= 11 else prod(num_list)