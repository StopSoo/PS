# 11051 : 이항 계수 2
# 모듈러 연산은 덧셈에 관해 다음과 같은 특성이 있다.
# (A mod N + B mod N) mod N = (A + B) mod N
# 따라서 이 문제에서 DP 테이블에 결과값이 나올 때마다 모듈러 연산을 수행하는 로직을 추가하면 문제를 해결할 수 있다. 
import sys
input = sys.stdin.readline
    
n, k = map(int, input().split())
D = [[0 for j in range(n+1)] for i in range(n+1)]

# D 테이블 초기화
for i in range(n+1):
    D[i][1] = i
    D[i][0] = 1
    D[i][i] = 1

for i in range(2, n+1):
    for j in range(1, i):
        D[i][j] = D[i-1][j] + D[i-1][j-1]   # 조합 점화식
        D[i][j] %= 10007    # 이렇게 더할 때마다 mod 연산을 해주는 게 포인트 !!

print(D[n][k])