# 1934 : 최소공배수

# 최대 공약수 함수를 재귀 함수로 구현
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

test = int(input())

for i in range(test):
    a, b = map(int, input().split())
    result = a * b // gcd(a, b)
    print(result)

# gcd 연산을 통해 a < b인 경우도 자동으로 swap되어 a > b인 상태로 바뀌기 때문에 신경 안 써도 된다 !