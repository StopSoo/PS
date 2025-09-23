# https://school.programmers.co.kr/learn/courses/30/lessons/389478

# 내 답안
def solution(n, w, num):
    position = []
    total_floor = (n + w - 1) // w
    for i in range(1, total_floor + 1):
        arr = []
        for j in range(1, w + 1): 
            if (i-1) * w + j <= n:
                arr.append((i-1) * w + j)
            else:
                arr.append(0)
        if i % 2 == 0: arr.reverse()     
        position.append(arr)

    floor = (num - 1) // w
    offset = (num - 1) % w
    if floor % 2 == 0: # 왼 -> 오
        j = offset
    else: # 오 -> 왼
        j = w - 1 - offset

    answer = 0 # 제거해야 할 박스의 수
    for f in range(floor, total_floor):
        if position[f][j] != 0:
            answer += 1

    return answer

# 리뷰
# 1. 복잡한 식은 변수를 사용해서 간단화하자
# 2. 몇 번 해보고 안되는 로직은 아예 지우고 새롭게 다시 생각해보자