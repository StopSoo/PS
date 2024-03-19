# 1010
import sys
input = sys.stdin.readline

# 팩토리얼 함수 정의
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

n = int(input())    # test case
i = 0   # 제어 변수 
while i < n:
    N, M = map(int, input().split())
    print(factorial(M) // (factorial(N) * factorial(M-N)))  # 조합의 수 계산
    i += 1