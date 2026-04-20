# https://school.programmers.co.kr/learn/courses/30/lessons/133502
# 260420 풀이

# 내 답변
# 꺠달은 점) 문자열을 비교하는 게 리스트를 비교하는 것보다 빠르다 (!)
def solution(ingredient):
    answer = 0
    temp = ''
    
    for i in ingredient:
        temp += str(i)
        if temp[-4:] == '1231':
            answer += 1
            temp = temp[:-4]
    
    return answer

# 다른 답변: 스택을 활용한다 (!)
def solution2(ingredient):
    s = []
    cnt = 0
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1, 2, 3, 1]:
            cnt += 1
            for _ in range(4): s.pop()
    
    return cnt