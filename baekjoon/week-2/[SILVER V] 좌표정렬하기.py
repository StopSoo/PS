# 파이썬에서의 정렬: 일반적으로 앞에 있는 원소를 기준으로 정렬 후 다음 원소에 대해 비교
T = int(input())

points = []
for _ in range(T):
  x, y = map(int, input().split())
  points.append([x, y])

points.sort()

for x, y in points:
  print(x, y)

# 더 짧은 코드
N = int(input())

points = [list(map(int, input().split())) for _ in range(N)]
points = sorted(points)

for x, y in points:
  print(x, y)