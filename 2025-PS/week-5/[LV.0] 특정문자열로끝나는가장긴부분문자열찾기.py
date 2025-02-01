# https://school.programmers.co.kr/learn/courses/30/lessons/181872

# 내 답안
# 4번째 줄에서 원래는 for문을 돌면서 조건에 맞지 않으면 제거하는 코드를 사용했음.
# 실시간으로 제거하면 배열 전체 순회가 불가능하므로, 리스트 컴프리헨션을 사용하는 것이 좋음 (!)
def solution(myString, pat):
    words = []
    for i in range(len(myString)): words.append(myString[:i+1])
    words = [word for word in words if word.endswith(pat)]
    return sorted(words)[len(words)-1]

# 간결하고 정확한 답안
# rfind(): 우측부터 찾아서 시작 인덱스를 반환
def solution(myString, pat):
    return myString[0:myString.rfind(pat)] + pat