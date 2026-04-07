# https://school.programmers.co.kr/learn/courses/30/lessons/161989
# 260407 풀이

# 내 답안
# 이 문제의 포인트는 "실제로 칠할 필요는 없다"는 것이다(!)
def solution(n, m, section):
    answer = 0
    last_painted = section[0] - 1 # 마지막으로 칠해진 구역의 끝 번호 저장하기 (!)
    
    for s in section:
        if s <= last_painted: continue
        else:
            answer += 1
            last_painted = s + (m - 1)
    
    return answer