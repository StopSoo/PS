# https://school.programmers.co.kr/learn/courses/30/lessons/120868
# 260403 풀이

# 내 답안
def solution(sides):
    answers = set()
    sides.sort()
    # 1) sides[1]이 가장 긴 변의 길이일 경우
    for new_side in range(1, sides[1] + 1):
        if sides[0] + new_side > sides[1]: answers.add(new_side)
    # 2) 새로운 변이 가장 긴 변의 길이일 경우
    for new_side in range(sides[1] + 1, sides[0] + sides[1]):
        answers.add(new_side)
    
    return len(answers)

# 다른 정답
# 근데 완벽히 이해되지는 않음 ...
def func(sides):
    return sum(sides) - max(sides) + min(sides) - 1
