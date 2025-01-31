# https://school.programmers.co.kr/learn/courses/30/lessons/181857

# 내 답안
# arr의 길이가 1000 이하라는 거지, 그 길이를 체크할 배열 pows는 1024까지 체크해야 함 (!)
def solution(arr):
    pows = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    if len(arr) not in pows:
        for i in range(len(pows)): 
            if pows[i] > len(arr):
                arr += [0] * (pows[i] - len(arr))
                return arr
    else: return arr

# 작성하다가 포기한 답안 완성
def solution(arr):
    answer = [2 ** i for i in range(11)]
    while len(arr) not in answer:
        arr.append(0)
    return arr