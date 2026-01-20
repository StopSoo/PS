# https://www.acmicpc.net/problem/11728
# 260120 풀이
# 알고리즘: 투포인터
# 시간: 2112ms
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))

answer = []
i, j = 0, 0
while i < len(A) and j < len(B):
    if A[i] <= B[j]:
        answer.append(A[i])
        i += 1
    else:
        answer.append(B[j])
        j += 1
answer += A[i:]
answer += B[j:]
print(*answer)

# 파이썬 내장 함수를 사용한 코드
# 시간: 1300ms
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))
print(*sorted(A + B))