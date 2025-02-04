# https://school.programmers.co.kr/learn/courses/30/lessons/120812

# 내 답안
def solution(array):
    counts = [0] * 1000
    for a in array: counts[a] += 1 # 개수 세기
    maxs = [count for count in counts if count == max(counts)] # 최빈값 리스트 구하기
    return -1 if len(maxs) > 1 else counts.index(max(counts))
