# https://school.programmers.co.kr/learn/courses/30/lessons/120869

# 내 답안
# for-else문: for문 중간에 종료되는 일 없이 마치면 else문이 실행됨 (!)
def solution(spell, dic):
    for word in dic:
        for s in spell:
            if word.count(s) != 1:
                break
        else:
            return 1
    return 2

# 정렬을 이용한 코드
def solution(spell, dic):
    for d in dic:
        if sorted(d) == sorted(spell):
            return 1
    return 2