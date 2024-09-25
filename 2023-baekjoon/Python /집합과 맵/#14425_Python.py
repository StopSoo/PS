# 14425 : 문자열 집합 
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

S = []
for i in range(N):  # 정해진 문자열 배열 입력 받기
    S.append(input())

count = 0
for i in range(M):
    word = input()
    if word in S:
        count += 1

print(count)

# 트라이 자료구조 공부하면 그걸로 풀어보기 !