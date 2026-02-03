# https://www.acmicpc.net/problem/2740
# 260203 풀이
# 알고리즘: 수학 / 구현
# 시간: 96ms

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

answer = [[0] * K for _ in range(N)]
for i in range(N):
    for j in range(K):
        answer[i][j] = sum(A[i][k] * B[k][j] for k in range(M))
# 출력
for row in answer:
    print(*row)

# 개선 부분 1: 리스트 컴프리헨션 내 sum 연산 -> 리스트를 매번 새로 생성하고 있다.
# 개선 전) answer[i][j] = sum([A[i][k] * B[k][j] for k in range(M)])
# 개선 후)answer[i][j] = sum(A[i][k] * B[k][j] for k in range(M))

# 개선 부분 2: 출력 부분에서 루프를 줄이기 위해 *(unpacking operator)를 사용한다.