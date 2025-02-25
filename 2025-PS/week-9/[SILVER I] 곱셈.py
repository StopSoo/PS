# https://www.acmicpc.net/problem/1629

# 내 답안
# 걸린 시간: 36ms
# 11401_이항계수3 문제 답안을 참고해서 풀이 (!) 
A, B, C = map(int, input().split())
# 풀이 포인트) 거듭제곱을 계산하는 함수/ (MOD 연산 미진행 시 값이 너무 커지므로)
# 이 때 분할 정복 & 나머지 연산을 적용.
# 분할 정복의 구체적 설명
# - B가 짝수일 때 A^B = (A^(B/2))^2
# - B가 홀수일 때 A^B = (A^(B//2))^2 * A
def power(a, b): 
  if b == 1: 
    return a % C
  else:
    temp = power(a, b // 2) 
    if b % 2 == 0:
      return temp * temp % C
    else:
      return temp * temp * a % C

print(power(A, B))