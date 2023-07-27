# 2869_commentary
import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())

days = (V - B) / (A - B)
print(int(days) if days == int(days) else int(days) + 1)

# days를 최소화시켜야 한다.
# days가 4.0인 경우 답은 4일이지만, 4.1인 경우 답은 5일이다. 