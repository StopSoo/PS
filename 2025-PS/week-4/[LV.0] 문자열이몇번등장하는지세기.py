# https://school.programmers.co.kr/learn/courses/30/lessons/181871

# 내 답안
def solution(myString, pat):
    count = 0 # 개수
    for i in range(len(myString)-len(pat)+1):
        if myString[i:i+len(pat)] == pat:
            count += 1
    return count

# 익혀야 할 함수를 사용한 코드
# enumerate(문자열) -> 인덱스, 값 반환
# startswith(문자열) -> 문자열이 해당 문자열로 시작하는지 여부를 반환
def solution(myString, pat):
    answer = 0
    for i, x in enumerate(myString) :
        if myString[i:].startswith(pat) :
            answer += 1
    return answer

# true 값을 반환하는 코드를 sum해서 총 개수를 구하는 코드
def solution(myString, pat):
    return sum(myString[i:i + len(pat)] == pat for i in range(len(myString)))