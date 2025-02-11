# https://www.acmicpc.net/problem/1463

# 내 답안
def makeOne(n, dp):
  if n == 1:
    return 0
  # 이미 계산된 값이면 그대로 반환
  if dp[n] != -1:
    return dp[n]

  res = makeOne(n - 1, dp) + 1  

  if n % 2 == 0:
    res = min(res, makeOne(n // 2, dp) + 1)

  if n % 3 == 0:
    res = min(res, makeOne(n // 3, dp) + 1)

  dp[n] = res
  return dp[n]

X = int(input())
dp = [-1] * (X + 1)  # 메모이제이션을 위한 리스트
print(makeOne(X, dp))

# 다른 사람의 답안
# 입력 처리를 open(0).read()로 한다는 점이 특이 (!) => 여러 줄 입력 받을 시 용이.
best = 0  # 최소 연산 횟수를 저장하는 변수

def calc(x, c = 0):
  global best
  if best and c == best:
    return  # 이미 최소 횟수(best)와 같은 경우 더 볼 필요 없음

  if x == 1:  # 목표 값(1)이 되었을 때
    best = c  # 현재 연산 횟수를 best에 저장
    return

  c += 1  # 연산 횟수 증가

  if x % 3 == 0:  # 3으로 나누어 떨어지면
    calc(x // 3, c)  
  if x % 2 == 0:  # 2로 나누어 떨어지면
    calc(x // 2, c)  
  calc(x - 1, c)  # 1을 빼는 연산 수행

# 입력 처리
calc(int(open(0).read()))
print(best)