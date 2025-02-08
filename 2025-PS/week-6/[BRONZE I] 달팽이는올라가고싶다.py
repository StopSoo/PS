# https://www.acmicpc.net/problem/2869

# 내 답안
# 반복문을 사용하지 않고, 수학적으로 접근 (!)
A, B, V = map(int, input().split())
# (A - B) * i + A >= V
print((V - A) // (A - B) + 1 if (V - A) % (A - B) == 0 else (V - A) // (A - B) + 2)

# 다른 사람들의 답안
# 올림 함수 사용하기 (!)
import math
A, B, V = map(int, input().split())
print(math.ceil((V - B) / (A - B)))