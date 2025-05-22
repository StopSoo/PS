# https://www.acmicpc.net/problem/12847

# 내 답안
# 걸린 시간: 84ms
# 알고리즘: 슬라이딩 윈도우(누적 합)
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) 
pay = [0] + list(map(int, input().split())) # 1기반 인덱스 
for i in range(1, n): # 누적합
  pay[i] += pay[i - 1]

max_profit = 0
for i in range(n - m + 1):
  if pay[i + m] - pay[i] > max_profit:
    max_profit = pay[i + m] - pay[i] # 갱신
print(max_profit)