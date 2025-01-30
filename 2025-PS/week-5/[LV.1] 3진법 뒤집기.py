# https://school.programmers.co.kr/learn/courses/30/lessons/68935?language=python3

# 내 답안
def solution(n):
    answer = ''
    while n != 1:
        answer += str(n % 3)
        n //= 3
    answer += '1'
    # 인덱스를 활용해 계산하기 위해 또 역전환함 
    answer = ''.join(list(reversed(answer)))
    result = 0
    for i in range(len(answer)):
        result += 3**int(i) * int(answer[i])
    return result

# 알아두어야 할 함수를 활용한 코드
# int(숫자로 이루어진 문자열, 해당 진법) -> 10진법으로 변환 (!)
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3) # 이 한 줄을 통해 10진법으로 변환 가능
    return answer