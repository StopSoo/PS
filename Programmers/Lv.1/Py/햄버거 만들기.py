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