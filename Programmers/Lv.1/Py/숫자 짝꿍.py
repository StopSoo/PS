# https://school.programmers.co.kr/learn/courses/30/lessons/131128
# 260410 풀이

# 깨달은 점 1) 개수를 셀 거면 딕셔너리 대신 Counter를 사용하자.
# 깨달은 점 2) 리스트에 추가할 때 append()와 extend()를 잘 구분해서 사용하자.
from collections import Counter

def solution(X, Y):
    counter_X = Counter(X)
    counter_Y = Counter(Y)

    answer = []
    for num in map(str, range(9, -1, -1)): # 크기가 큰 숫자부터 추가하기
        count = min(counter_X[num], counter_Y[num])
        answer.extend([num] * count)
        
    if not answer: 
        return "-1"
    
    result = ''.join(answer)
    
    return "0" if result[0] == "0" else result