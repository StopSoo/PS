# https://www.acmicpc.net/problem/14425

# 내 답안
import sys
input = sys.stdin.readline # 표준 입출력

N, M = map(int, input().split())
answers = [input() for _ in range(N)]
str_list = [input() for _ in range(M)]
print(sum([1 for word in str_list if word in answers]))