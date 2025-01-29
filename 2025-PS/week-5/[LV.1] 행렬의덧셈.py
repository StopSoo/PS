# https://school.programmers.co.kr/learn/courses/30/lessons/12950?language=python3

# 내 답안 -> 정석대로 함
# 제어변수 범위 설정하는데 시간이 좀 걸림, 그리고 pythonic하지 않음
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        row = []
        for j in range(len(arr1[0])):
            row.append(arr1[i][j] + arr2[i][j])
        answer.append(row)
    return answer

# 모범 답안
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a,b)] for a, b in zip(A,B)]
    return answer