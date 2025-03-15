# https://www.acmicpc.net/problem/13909

# 내 답안
# 걸린 시간: 36ms
# 아이디어: 제곱수는 약수의 개수가 홀수이다. 따라서 1이다.
# (1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1) -> 제곱수마다 1이다.
import math

N = int(input())
print(len(range(1, int(math.sqrt(N))+1))) # 제곱수의 개수를 반환