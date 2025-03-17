# https://www.acmicpc.net/problem/4134

# 내 답안
# 걸린 시간: 2868ms 
# 처음엔 에라토스테네스의 체를 사용했는데, 수 범위가 너무 넓어서 다른 방법을 고안.
# for문을 돌 때 int(루트 n)+1까지 돈다는 게 포인트 (!)
import math

T = int(input())
numbers = [int(input()) for _ in range(T)]

for number in numbers:
  if number == 0 or number == 1: # 명시적으로 지정하기.
    print(2)
    continue
  s = number
  while True:
    flag = True
    for i in range(2, int(math.sqrt(s))+1): # 합성수인지 체크. 
      if s % i == 0: 
        flag = False
        break
    if flag:
      print(s)
      break
    else:
      s += 1