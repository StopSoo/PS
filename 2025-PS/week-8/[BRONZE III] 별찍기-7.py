# https://www.acmicpc.net/problem/2444

# 내 답안
# 걸린 시간: 36ms 
# 출력 형식 오류 -> * 우측에 있는 띄어쓰기는 삭제해주면 됨 (!)
N = int(input())

for i in range(1, N+1):
  print(' '*(N-i) + '*'*(2*i-1))
for i in range(N-1, 0, -1):
  print(' '*(N-i) + '*'*(2*i-1))