# https://school.programmers.co.kr/learn/courses/30/lessons/142086?language=python3

# 내 답안
# 답은 나오지만 뭔가 복잡함
def solution(s):
    position = [-1] * 26
    answer = []
    for i in range(len(s)):
        if position[ord(s[i]) - ord('a')] == -1:
            position[ord(s[i]) - ord('a')] = i
            answer.append(-1)
        else:
            answer.append(i - (position[ord(s[i]) - ord('a')]))
            position[ord(s[i]) - ord('a')] = i # 재업데이트
    return answer

# 좀 더 정돈된 코드
# 내가 사용한 position 배열보다 dictionary를 사용하는 편이 나을 듯
def solution(s):
    answer = []
    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
        dic[s[i]] = i

    return answer