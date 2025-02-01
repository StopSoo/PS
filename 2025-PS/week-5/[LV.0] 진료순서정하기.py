# https://school.programmers.co.kr/learn/courses/30/lessons/120835

# 내 답안
# enumerate의 두 번째 인자를 시작 인덱스 (!)
# 첫 답안은 딕셔너리 썼었는데 구지임 
def solution(emergency):
    sorted_emergency = sorted([(x, i) for i, x in enumerate(emergency)], reverse=True)
    answer = [0] * len(emergency)
    for rank, (_, idx) in enumerate(sorted_emergency, 1):
        answer[idx] = rank
    return answer

# 좀 더 간결한 답안
def solution(emergency):
    return [sorted(emergency, reverse=True).index(e) + 1 for e in emergency]