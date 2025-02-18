# https://www.acmicpc.net/problem/10870

# 내 답안
# 걸린 시간: 32ms
# 재귀 함수를 사용하는 일반적인 방법
# but, 연산 횟수가 너무 많음
def Fibonacci(n):
  if n == 0: return 0
  if n == 1: return 1
  return Fibonacci(n-2) + Fibonacci(n-1)

n = int(input())
print(Fibonacci(n))

# 메모이제이션을 사용하는 방법
def Fibonacci(n):
  global arr

  if arr[n] != -1:
    return arr[n]
  
  arr[n] = Fibonacci(n-2) + Fibonacci(n-1)
  return arr[n]

n = int(input())

arr = [-1] * (n + 2)  # 배열 초기화
arr[0] = 0
arr[1] = 1
print(Fibonacci(n))