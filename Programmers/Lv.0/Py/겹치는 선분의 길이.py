# https://school.programmers.co.kr/learn/courses/30/lessons/120876
# 260403 풀이

# 내 답안
# 선분의 구간이 -100 ~ 100까지로 작기 때문에 배열을 만들어서 체크하는 방식으로 계산
def solution(lines):
    arr = [0] * 200 # -100 ~ 99
    for s, e in lines:
        for i in range(s, e):
            arr[i + 100] += 1
    return sum([1 for a in arr if a >= 2])

# 다른 사람의 답안
def func(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])