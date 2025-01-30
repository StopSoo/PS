# https://school.programmers.co.kr/learn/courses/30/lessons/159994?language=python3

# 내 답안
# 너무 길고 지저분 .. 근데 정리할 방법이 생각이 안 났음
def solution(cards1, cards2, goal):
    for g in goal:
        if cards1 == []:
            if g == cards2[0]: 
                cards2.remove(cards2[0])
                continue
            else: return "No"
        elif cards2 == []:
            if g == cards1[0]: 
                cards1.remove(cards1[0])
                continue
            else: return "No"
        if g == cards1[0]:
            cards1.remove(cards1[0])
        elif g == cards2[0]:
            cards2.remove(cards2[0])
        else:
            return "No"
    return "Yes"

# 간결한 답안
# pop(인덱스): 해당 인덱스의 원소를 제거
def solution(cards1, cards2, goal):
    for g in goal:
      # 문장의 길이를 먼저 확인해서 오류를 방지
        if len(cards1) > 0 and g == cards1[0]:
            cards1.pop(0)       
        elif len(cards2) > 0 and g == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"