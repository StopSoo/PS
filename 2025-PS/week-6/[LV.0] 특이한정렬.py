# https://school.programmers.co.kr/learn/courses/30/lessons/120880

# 내 답안
# key로 정렬 기준을 줄 것. 기준은 앞에서부터 적용
def solution(numlist, n):
    return sorted(numlist, key=lambda x: [abs(x-n), n-x])