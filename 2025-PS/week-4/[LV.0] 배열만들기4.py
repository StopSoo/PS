# https://school.programmers.co.kr/learn/courses/30/lessons/181918

# 내 답안
# del -> 리스트의 원소 삭제
def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if not stk:
            stk.append(arr[i])
            i += 1
        elif stk and stk[len(stk)-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        elif stk and stk[len(stk)-1] >= arr[i]:
            del stk[len(stk)-1]
    return stk

# 더 간결한 답안
# for문도 사용할 수 있다는 점
# 리스트의 마지막 원소 삭제할 때 -> pop()
def solution(arr):
    stk = []
    for i in range(len(arr)):
        while stk and stk[-1] >= arr[i]:
            stk.pop()
        stk.append(arr[i])
    return stk