# https://school.programmers.co.kr/learn/courses/30/lessons/181931

# 내 답안
def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        answer += (a + i * d) * included[i]
    return answer

# 숏코딩
# enumerate: 인덱스, 값 꺼내기
def solution(a, d, included):
    return sum(a + i * d for i, f in enumerate(included) if f)