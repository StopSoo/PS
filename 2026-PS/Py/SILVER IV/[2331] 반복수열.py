# https://www.acmicpc.net/problem/2331
# 260131 풀이
# 알고리즘: 구현
# 시간: 28ms

A, P = map(int, input().split())
numbers = [A]
while True:
    result = sum([int(num) ** P for num in str(numbers[-1])])
    if result in numbers: 
        numbers = numbers[:numbers.index(result)]
        break
    else: 
        numbers.append(result)

print(len(numbers))