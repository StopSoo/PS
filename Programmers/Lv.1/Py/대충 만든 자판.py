# https://school.programmers.co.kr/learn/courses/30/lessons/160586
# 260410 풀이

def solution(keymap, targets):
    answer = []
    keyCount = { chr(i + 65): -1 for i in range(26) } # 가장 적은 키 터치 수 저장하는 딕셔너리
    
    for i in range(26):
        ch = chr(i + 65)
        indexs = [km.index(ch) for km in keymap if ch in km]
        if indexs: 
            keyCount[ch] = min(indexs) + 1

    for target in targets:
        s = 0
        for t in target:
            if keyCount[t] != -1:
                s += keyCount[t]
            else: # 해당 문자를 입력할 수 없는 경우
                s = -1
                break
        
        answer.append(s)
    
    return answer
