# https://school.programmers.co.kr/learn/courses/30/lessons/181836

# 내 답안
# 이렇게 어렵게 풀다니 ...
def solution(picture, k):
    words = ''.join([x * k for pic in picture for i in range(k) for x in pic])
    return [words[i:i+len(picture[0])*k] for i in range(0, len(picture[0])*k*len(picture)*k, len(picture[0])*k)]

# 간결하고 직관적인 답안
def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        for _ in range(k):
            answer.append(picture[i].replace('.', '.' * k).replace('x', 'x' * k))
    return answer