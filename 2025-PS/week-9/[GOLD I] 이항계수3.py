# https://www.acmicpc.net/problem/11401

# 답안
# 알고리즘 유형: 분할 정복, 페르마의 소정리
# 걸린 시간: 828ms
# 풀이 포인트 1) 나머지 연산의 분배 법칙 -> 분배 법칙이 성립하지는 않고, 아래 형태처럼 바꿔주면 됨
# (A + B) % p = ((A % p) + (B % p)) % p
# (A x B) % p = ((A % p) x (B % p)) % p
# (A - B) % p = ((A % p) - (B % p) + p) % p

# 풀이 포인트 2) 페르마의 소정리 -> 분수 형태를 곱셈 형태로 변경 (!)
# p가 소수, a가 정수일 때 a^p === a (mod p): 합동이다
# 이 식의 양변을 a^2으로 나눠주면 a^(p-2) === (1/a)(mod p)
# 정리하면, NCK % p = N!((N-K)!K!)^(p-2) % p
N, K = map(int, input().split())
p = 1000000007

# 거듭제곱을 계산 (분할 정복 & 나머지 연산 적용)
def power(a, b): 
  if b == 1: 
    return a % p
  else:
    temp = power(a, b // 2) 
    if b % 2 == 0:
      return temp * temp % p 
    else:
      return temp * temp * a % p 

# 팩토리얼 값 계산 (나머지 연산 적용)
def factorial(n):
  result = 1
  for i in range(2, n+1):
    result = (result * i) % p
  return result

up = factorial(N)
down = power(factorial(N-K) * factorial(K), p-2)

print((up * down) % p)