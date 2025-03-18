# https://www.acmicpc.net/problem/6064

# 내 답안
# 걸린 시간: 1532ms
# 내 아이디어: M과 N의 갭과 x와 y의 갭을 맞추고, M과 x의 갭과 N과 y의 갭을 맞춘다. -> 예시로 몇 번 해보니 아닌 것 같다는 판단을 함.
# 받은 힌트: 나머지 연산을 잘 생각해보자 (!)
import sys
import math

input = sys.stdin.readline
T = int(input())

for _ in range(T):
  M, N, x, y = map(int, input().split())

  lcm_val = (M*N) // math.gcd(M, N) # 최소공배수 구하기

  for k in range(x, lcm_val+1, M): # k%M==x를 만족시키기 위함(!)
    if (k-1) % N + 1 == y: # 1부터 시작하므로 맞춰주기 위함(!)
      print(k)
      break
  else: # 없다면 -1 출력
    print(-1)

