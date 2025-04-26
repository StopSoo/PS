# https://www.acmicpc.net/problem/12871

# 내 답안
# 걸린 시간: 40ms
# 아이디어: 두 문자열의 길이를 최소공배수 값으로 맞춘다!
import math 

s = input()
t = input()
lcm = math.lcm(len(s), len(t))
s = s * (lcm // len(s))
t = t * (lcm // len(t))

if s == t: print(1)
else: print(0)

# 더 간단한 답안
a = input()
b = input()
if a + b == b + a: print(1)
else: print(0)