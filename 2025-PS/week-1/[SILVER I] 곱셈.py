# 풀이 1
n = int(input())
m = input()

print(n * int(m[2]))
print(n * int(m[1]))
print(n * int(m[0]))
print(n * int(m))

# 풀이 2
n = int(input())
m = int(input())

print(n * (m % 10))
print(n * (m // 10 % 10))
print(n * (m // 100))
print(n * m)

# 모범 답안
n = int(input())
m = int(input())

for num in reversed(str(m)):  # 문자열은 반복문 사용 가능
  print(n * int(num))
print(n * m)