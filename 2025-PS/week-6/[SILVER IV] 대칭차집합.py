# https://www.acmicpc.net/problem/1269

# 내 답안
# 교집합(&) / 합집합(|) / 차집합(-) / 대칭 차집합(^)
countA, countB = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
print(len(A - B) + len(B - A))