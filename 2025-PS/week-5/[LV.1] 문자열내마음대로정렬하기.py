# https://school.programmers.co.kr/learn/courses/30/lessons/12915

# 내 답안
# 이 문제는 살짝 아이디어 싸움이라는 생각이 들었음
def solution(strings, n):
    new_strings = [x[n] + x[:n] + x[n+1:] for x in strings]
    new_strings.sort()
    return [x[1:n+1] + x[0] + x[n+1:] for x in new_strings]

# 다른 사람의 답안
# sorted 함수의 두 번째 인자로 key를 넣을 수 있다 (!)
def strange_sort(strings, n):
    return sorted(strings, key=lambda x: x[n])