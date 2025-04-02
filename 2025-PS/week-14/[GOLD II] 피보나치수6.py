# https://www.acmicpc.net/problem/11444

# 답안
# 걸린 시간: 44ms
# 아이디어: 피보나치 수가 행렬 [[1,1], [1,0]]의 거듭제곱으로 구해질 수 있다 (!)
def matrix_power(base, exp, MOD):
  result = [[1, 0], [0, 1]]  # 단위 행렬
  
  while exp: # 분할정복 사용 (!)
    if exp % 2:  # 홀수이면 base를 result에 곱해줌
      result = multiply(result, base, MOD)
    base = multiply(base, base, MOD)  # base = base^2
    exp //= 2  # 지수를 절반으로 줄임
  
  return result

def multiply(A, B, MOD):
  return [
    [
      (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
      (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD
    ],
    [
      (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
      (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD
    ]
  ]

n = int(input())
MOD = 1000000007
base_matrix = [[1, 1], [1, 0]]

if n == 1:
  print(1)
else:
  result_matrix = matrix_power(base_matrix, n - 1, MOD)
  print(result_matrix[0][0])  # F(n) 값 출력