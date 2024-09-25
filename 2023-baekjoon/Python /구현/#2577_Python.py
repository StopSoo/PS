# 2577 : 숫자의 개수

# 세 숫자 입력 받기
A = int(input())
B = int(input())
C = int(input())

result = str(A * B * C)
array = [0] * 10    # 숫자의 개수를 담을 배열 초기화

for i in range(len(result)):
    array[int(result[i])] += 1

# print
for i in range(10):
    print(array[i])