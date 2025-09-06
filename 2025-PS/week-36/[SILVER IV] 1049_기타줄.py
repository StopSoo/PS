# https://www.acmicpc.net/problem/1049

# 내 답안
# 걸린 시간: 36ms
# 알고리즘: 그리디 
# 내가 푼 코드가 그리디 알고리즘으로 푼 코드인 이유
# "항상 그 순간에 더 싼 선택지를 골라서 최소 비용을 구함."

# 주의할 점
# 1) 패키지 가격보다 개별*6 가격이 더 쌀 수 있다.
# 2) 패키지 구매 후 나머지 개수대로 개별 줄을 사는 것보다 패키지 하나를 더 사는 게 더 쌀 수 있다.
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
packages = [] # 세트 가격
each = [] # 개별 줄 
for _ in range(M):
  p, e = map(int, input().strip().split())
  packages.append(p)
  each.append(e)
# 가장 싼 가격 찾기
packages.sort()
each.sort()

money = 0
# 1. 6개 세트 계산 (뭐가 더 이득인지 비교)
if packages[0] < each[0] * 6: 
  money += (N // 6) * packages[0]
elif packages[0] >= each[0] * 6:
  money += (N // 6) * (each[0] * 6)
# 2. 나머지 계산 (뭐가 더 이득인지 비교)
if packages[0] < each[0] * (N % 6):
  money += packages[0]
elif packages[0] >= each[0] * (N % 6):
  money += each[0] * (N % 6)

print(money)