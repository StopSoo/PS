# https://school.programmers.co.kr/learn/courses/30/lessons/12982?language=python3

# 내 답안
# 내 답안에서 생략되어도 되는 부분은 빼는 개수를 정해서 종류별로 빼는 것이다.
# 사실 가장 큰 수대로 차례로 빼면 그것보다 작은 수들을 빼는 것은 체크하지 않아도 되므로!
def solution(d, budget):
    if sum(d) <= budget: 
        return len(d)
    else:
        d.sort()
        for count in range(1, len(d)+1): # 빼는 개수
            for i in range(len(d)):
                if sum(d) - sum(d[i:i+count]) <= budget: 
                    return len(d) - count

# 더 간단한 답안
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)