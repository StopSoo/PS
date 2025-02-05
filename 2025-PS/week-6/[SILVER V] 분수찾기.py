# https://www.acmicpc.net/problem/1193

# 내 답안 -> 답은 맞게 나오지만 백준에서는 틀렸음
import sys
input = sys.stdin.readline
print = sys.stdout.write

X = int(input().strip())
for i in range(1, 4500):
  if X > (i * (i - 1)) // 2 and X <= (i * (i + 1)) // 2:
    # 합은 i+1
    left = (X - sum(range(0, i)))
    right = (i + 1) - left
    print(f'{left}/{right}\n')
    break

# 효율적인 정답
import sys
input = sys.stdin.readline

X = int(input())
line = 1

while X > line:
  X -= line
  line += 1

if line % 2 == 0:
  up = X
  down = line - X + 1
else:
  up = line - X + 1
  down = X

print(f'{up}/{down}')