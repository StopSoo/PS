# 1269
import sys
input = sys.stdin.readline

n, m = map(int, input().split())    # 배열에서 원소의 개수
A = set(map(int, input().split())) # A 집합
B = set(map(int, input().split())) # B 집합

# print(len(A) - len(A&B) + len(B) - len(A&B))
print(len(A-B) + len(B-A))