# https://school.programmers.co.kr/learn/courses/30/lessons/12930?language=python3

# 내 답안
def solution(s):
    answer = ''
    ind = 0 # 단어의 인덱스
    for i in range(len(s)): # 문자열 전체 인덱스
        if s[i] == ' ': 
            ind = 0 # 단어 인덱스 초기화
            answer += ' ' # 공백 추가
            continue
        
        if ind % 2 == 0: answer += s[i].upper()
        else: answer += s[i].lower()
        ind += 1
    return answer

# 한 줄 답안
# lambda식 활용 체크
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))