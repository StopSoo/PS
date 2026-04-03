# https://school.programmers.co.kr/learn/courses/30/lessons/120843
# 260403 풀이

# 내 답안
# deque를 사용하기
from collections import deque

def solution(numbers, k):
    deq = deque(numbers)
    for _ in range(k - 1): deq.rotate(-2)
    return deq[0]
        
# 다른 사람의 답안
def func(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)]