# 5073 : 삼각형과 세 변
import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())

    if a == b == c == 0:
        break
    elif a == b == c:
        print('Equilateral')
    elif max(a, b, c) < sum([a, b, c]) - max(a, b, c):
        if a == b or b == c or c == a:
            print('Isosceles')
        else:
            print('Scalene')
    else:
        print('Invalid')