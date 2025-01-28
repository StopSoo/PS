# https://school.programmers.co.kr/learn/courses/30/lessons/181838

# 내 답안 -> 완전 노가다 (맞았지만 효율성 제로)
def solution(date1, date2):
    if date1[0] > date2[0]: return 0
    elif date1[0] == date2[0]:
        if date1[1] > date2[1]: return 0
        elif date1[1] == date2[1]:
            if date1[2] >= date2[2]: return 0
            else: return 1
        else: return 1
    else:
        return 1

# 간결한 답안
# 리스트 간에도 부등호 사용이 가능하다!
def solution(date1, date2):
    return int(date1 < date2)

# 내가 실제로 사용할 수 있을 것 같은 답안
# 값이 같으면 다음 반복문으로 넘어간다는 점
def solution(date1, date2):
    for i in range(3):
        if date1[i] < date2[i]: return 1
        elif date2[i] < date1[i]: return 0
    return 0