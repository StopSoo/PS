# https://school.programmers.co.kr/learn/courses/30/lessons/155652
# 260410 풀이

# 내 답안
# 포인트 1) 리스트에서 특정 원소 제거하기 -> list.remove(원소)
def solution(s, skip, index):
    answer = ''
    alphas = [chr(97 + i) for i in range(26)]
    for sk in skip: alphas.remove(sk) # 알파벳 목록에서 skip 문자들 제거
    l_alphas = 26 - len(skip)
    
    for ch in s:
        answer += alphas[(alphas.index(ch) + index) % l_alphas]    
    return answer