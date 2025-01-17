# https://school.programmers.co.kr/learn/courses/30/lessons/181923

# 내 답안
# 리스트 안에 반복문, 조건문 사용하기
# 빈 배열은 False를 반환
def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        array = [x for x in arr[s:e+1] if x > k]
        if not array:
            answer.append(-1)
        else:
            answer.append(min(array))
    return answer