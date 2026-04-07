# https://school.programmers.co.kr/learn/courses/30/lessons/133499
# 260407 풀이

# 내 답안
def solution(babbling):
    answer = 0
    pos = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        for p in pos:
            if p * 2 not in word: # 금지된 패턴(같은 단어의 연속)이 있는지 체크(!)
                word = word.replace(p, ' ')
            else:
                break
        if word.strip() == '': answer += 1
        
    return answer