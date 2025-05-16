# https://www.acmicpc.net/problem/1992

# 내 답안
# 걸린 시간: 40ms
# 입/출력 형태를 잘 확인하고 코드를 짜자.
# 재귀에서는 되도록이면 전역 변수를 사용하지 말자.
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N = int(input())
arr = list(list(map(int, list(input().strip()))) for _ in range(N))

def check(n, arr):
  if all(x == 1 for row in arr for x in row): return '1'
  elif all(x == 0 for row in arr for x in row): return '0'
  else: 
    top_left = check(n // 2, [row[:n//2] for row in arr[:n//2]])
    top_right = check(n // 2, [row[n//2:] for row in arr[:n//2]])
    bottom_left = check(n // 2, [row[:n//2] for row in arr[n//2:]])
    bottom_right = check(n // 2, [row[n//2:] for row in arr[n//2:]])
  
  return f"({top_left}{top_right}{bottom_left}{bottom_right})" # f-string으로 반환하기

print(check(N, arr))