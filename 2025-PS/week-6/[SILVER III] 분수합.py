# https://www.acmicpc.net/problem/1735

# 내 답안
from math import gcd
s1, m1 = map(int, input().split())
s2, m2 = map(int, input().split())
res1, res2 = (s1*m2 + s2*m1), m1*m2
print(res1 // gcd(res1, res2), res2 // gcd(res1, res2))