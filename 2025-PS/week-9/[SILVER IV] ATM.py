# https://www.acmicpc.net/problem/11399

# 내 답안
# 걸린 시간: 36ms
# 돈 인출하는 데 필요한 시간의 총합의 최솟값 -> 리스트의 오름차순 정렬이 필요.
N = int(input())
P = sorted(list(map(int, input().split()))) # 돈 인출 시간
result = 0
for i, time in enumerate(P):
  # 방법 1
  result += (time * (N-i))
  # 방법 2: 리스트를 인덱스1부터 마지막까지 돌면서 원소마다 누적합을 계산
print(result)