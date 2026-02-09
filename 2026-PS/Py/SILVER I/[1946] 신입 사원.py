# https://www.acmicpc.net/problem/1946
# 260204 풀이
# 알고리즘: 그리디 / 정렬
# 시간:

# 내 답안
# 깨달은 점 1: 문제를 잘 읽자! "순위"
# 깨달은 점 2: 반복 횟수를 최소화하자.
import sys
input = sys.stdin.readline

T = int(input())
answers = []
for _ in range(T):
    N = int(input().strip())
    scores = sorted(list(list(map(int, input().strip().split())) for _ in range(N)))

    count = 0
    min_score = scores[0][1]
    for i in range(N):
        if scores[i][1] <= min_score: # 어차피 서류 순위로 정렬되어 있으니까 이 방식이 굿.
            count += 1
            min_score = scores[i][1]
    answers.append(count)

print(*answers, sep='\n')