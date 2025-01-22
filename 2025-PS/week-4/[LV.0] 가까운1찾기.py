# https://school.programmers.co.kr/learn/courses/30/lessons/181898

# 내 답안
def solution(arr, idx):
    for i in range(len(arr[idx:])):
        if arr[i+idx] == 1:
            return i + idx
    return -1

# 배우면 좋을 답안
# 리스트.index(값, 시작 인덱스)
# try / except 문
def solution(arr, idx):
    answer = 0
    try:
        answer = arr.index(1, idx)
    except:
        answer = -1
    return answer