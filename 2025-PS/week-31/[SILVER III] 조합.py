# https://www.acmicpc.net/problem/2407

# 내 답안
# 걸린 시간: 36ms
# combinations 모듈을 사용하기에는 너무 시간 초과세여 ~ 그냥 조합 공식 쓰실게요 ~
# 중요한 점(!!): //는 정밀도 손실이 없고, /는 부동소수점 나눗셈을 수행하기에 큰 숫자를 다루면 오차가 발생한다.
# / 연산 후 int() 변환을 진행할 경우 이미 오차가 생긴 값을 변환하는 것이기 때문에 틀리게 된다.
from math import factorial

n, m = map(int, input().split())
print(factorial(n) // (factorial(m) * factorial(n - m)))