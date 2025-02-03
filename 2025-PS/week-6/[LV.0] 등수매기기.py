# https://school.programmers.co.kr/learn/courses/30/lessons/120882

# 내 답안
def solution(score):
    avgs = []
    for eng, mat in score: avgs.append((eng+mat)/2)
    avgs.sort(reverse=True)
    
    answer = [0] * len(score)
    for avg in avgs:
        inds = [i for i, (eng, mat) in enumerate(score) if (eng+mat)/2 == avg]
        for ind in inds:
            answer[ind] = avgs.index(avg)+1
    return answer

# 비상한 답안
# 일단 평균을 구할 필요가 없음
# index()는 처음 인덱스를 반환한다는 것을 활용해서 간단하게 해결 가능 (!)
def solution(score):
    a = sorted([sum(i) for i in score], reverse = True)
    return [a.index(sum(i))+1 for i in score]