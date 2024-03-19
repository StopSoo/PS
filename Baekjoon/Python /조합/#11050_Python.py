# 11050
# 팩토리얼 함수 구현
# n이 0인 경우와 1인 경우 모두 체크할 것 !!
def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n-1)

N, K = map(int, input().split())
print(factorial(N) // (factorial(K) * factorial(N-K)))
