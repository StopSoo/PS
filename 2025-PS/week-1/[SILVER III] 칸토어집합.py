# https://www.acmicpc.net/problem/4779

# 내 답안
# 알고리즘 유형: 재귀함수 사용 / 분할 정복
# 입출력 조건을 잘 읽자 ^.^
def f(n):
  if n == 0:
    return "-"
  else:
    return f(n-1) + (" " * (3 ** (n-1))) + f(n-1)

while True:
  try:
    n = int(input())
    result = f(n)
    print(result)
  except:
    break

# bottom-up 방식 (*)
# 시간 복잡도 계산 후 시간 초과가 아니기 때문에 이 방식도 ok
ans = ['' for _ in range(13)] # 초기화
ans[0] = '-'

for i in range(1, 13):
  ans[i] = ans[i-1] + (' ' * (3 ** (i-1))) + ans[i-1]

while True:
  try:
    n = int(input())
    print(ans[n])
  except:
    break