# https://school.programmers.co.kr/learn/courses/30/lessons/120921

# 내 답안
def solution(A, B):
    words = [A]
    for i in range(len(A)-1):
        A = A[-1] + A[:len(A)-1]
        words.append(A)
    return words.index(B) if B in words else -1