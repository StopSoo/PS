# https://www.acmicpc.net/problem/11720

# 내 답안
# 숫자로 이루어진 문자열을 하나씩 분리할 때 list(문자열)
N = int(input())
numbers = input()
print(sum(map(int, list(numbers))))