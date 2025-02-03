# https://school.programmers.co.kr/learn/courses/30/lessons/181851

# 내 답안
def solution(rank, attendance):
    inds = []
    for i in range(1, len(rank)+1):
        if attendance[rank.index(i)] and len(inds) != 3: inds.append(rank.index(i))
    return 10000 * inds[0] + 100 * inds[1] + inds[2]

# 배우고 싶은 답안
# enumerate 써서 인덱스랑 같이 정렬하기
def solution(rank, attendance):
    arr = sorted([(x, i) for i, x in enumerate(rank) if attendance[i]])
    return arr[0][1] * 10000 + arr[1][1] * 100 + arr[2][1]