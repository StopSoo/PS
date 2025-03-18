# https://www.acmicpc.net/problem/14215

# 내 답안
# 걸린 시간: 36ms
# 아이디어: 삼각형을 만들 수 있는 조건 (c가 가장 클 때)=> a + b > c
a, b, c = map(int, input().split())
max_length = max(a, b, c)
x, y = 0, 0
l = [a, b, c]
for idx, length in enumerate(l):
  if length == max_length:
    l.pop(idx)
    x, y = l[0], l[1]
    break
if x + y > max_length:
  print(x + y + max_length)
else:
  while x + y <= max_length:
    max_length -= 1
  print(x + y + max_length)

# 좀 더 간결한 답안
number= list(map(int, input().split()))

perimeter_triangle = 0
sum_all = sum(number) # 주어진 세 막대의 합을 구해놓기

for i in number:
  if sum_all - i > i:
    perimeter_triangle += i
  else:
    perimeter_triangle += sum_all - i - 1

print(perimeter_triangle)