# https://school.programmers.co.kr/learn/courses/30/lessons/120885

# 내 답안
# int(값, 진법): 해당 진법으로 표시된 값을 10진법으로 변환
# 처음에 통과 안됐던 이유: 0이라는 예외가 있었어서!
def solution(bin1, bin2):
    value = int(bin1, 2) + int(bin2, 2)
    if value == 0: return "0"
    answer = ''
    while value != 1:
        answer += str(value % 2)
        value //= 2
    answer += '1'
    return answer[::-1]

# 간결한 답안
# 배워둬야 할 함수: bin() -> 이진수로 변환 (ex> 0b1011처럼 앞에 0b가 붙음)
def solution(bin1, bin2):
    answer = bin(int(bin1, 2) + int(bin2, 2))[2:]
    return answer