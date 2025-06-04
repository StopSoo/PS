# https://www.acmicpc.net/problem/2096

# 내 답안
# 걸린 시간: 240ms
# 알고리즘: DP
# 첫 코드 -> 메모리 초과 (4MB 제한): N이 최대 10만인데, 가로 6 세로 10만으로 배열을 짬.
# 보완 -> 지금까지 중에 최고/최저 값들만 저장해도 괜찮다!
import sys
input = sys.stdin.readline

N = int(input())
l = list(map(int, input().strip().split()))
highest = [l[0], l[1], l[2]]
lowest = [l[0], l[1], l[2]]
for i in range(1, N):
  arr = list(map(int, input().strip().split()))
  temp_highest = highest[:]
  temp_lowest = lowest[:]

  highest[0] = max(temp_highest[0], temp_highest[1]) + arr[0]
  lowest[0] = min(temp_lowest[0], temp_lowest[1]) + arr[0]

  highest[1] = max(temp_highest[0], temp_highest[1], temp_highest[2]) + arr[1]
  lowest[1] = min(temp_lowest[0], temp_lowest[1], temp_lowest[2]) + arr[1]

  highest[2] = max(temp_highest[1], temp_highest[2]) + arr[2]
  lowest[2] = min(temp_lowest[1], temp_lowest[2]) + arr[2]

print(max(highest), min(lowest))