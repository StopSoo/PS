# https://www.acmicpc.net/problem/1629

# 내 답안
# 걸린 시간:
# 알고리즘: 분할정복을 이용한 거듭제곱
A, B, C = map(int, input().split())
# 풀이 포인트 1) 거듭제곱을 계산하는 함수 (MOD 연산 미진행 시 값이 너무 커지므로)
# 거듭제곱을 계산 (분할 정복 & 나머지 연산 적용)
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