# https://www.acmicpc.net/problem/2745

# 내 답안
# 걸린 시간: 36ms
N, B = input().split()
result = 0
for i, n in enumerate(reversed(list(N))):
  if n.isdigit():
    result += int(n) * (int(B) ** i)
  else:
    result += (ord(n)-55) * (int(B) ** i)
print(result)