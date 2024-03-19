# 10773

K = int(input())    # 수의 개수
stack = []

for i in range(K):
    number = int(input())
    if number != 0:
        stack.append(number)
    else:
        stack.pop()

print(sum(stack))