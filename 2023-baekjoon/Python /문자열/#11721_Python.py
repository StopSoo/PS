# 11721 : 열 개씩 끊어 출력하기
import sys
input = sys.stdin.readline

word = input()
i = 0
while i < len(word):
    if i != 0 and i % 10 == 0:
        print()
    print(word[i], end="")
    i += 1