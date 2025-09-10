# https://www.acmicpc.net/problem/24460

# 내 답안
# 걸린 시간: 992ms
# 알고리즘: 분할정복 / 재귀
# 중간에 답이 이상하게 나오는 문제가 있었는데, 함수 안에서 arr 대신 pos를 사용해서 ..! -> 정신 차리세욥.
# 이 코드도 백준에서 충분히 통과하지만, 배열을 매번 슬라이싱해서 복사해서 넘기는 건 비효율적이다.
import sys
input = sys.stdin.readline

N = int(input())
pos = list(list(map(int, input().strip().split())) for _ in range(N))

def find_number(n, arr):
  if n == 1:
    return arr[0][0]

  first = find_number(n//2, [row[:n//2] for row in arr[:n//2]])
  second = find_number(n//2, [row[n//2:] for row in arr[:n//2]])
  third = find_number(n//2, [row[:n//2] for row in arr[n//2:]])
  fourth = find_number(n//2, [row[n//2:] for row in arr[n//2:]])

  new_arr = sorted([first, second, third, fourth])
  return new_arr[1]

print(find_number(N, pos))

# 개선 코드
# 걸린 시간: 532ms
# 배열 슬라이싱 후 복사해서 전달하는 방식을 개선한 코드.
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N = int(input())
pos = [list(map(int, input().strip().split())) for _ in range(N)]

def find_number(r, c, n):
  if n == 1:
    return pos[r][c]

  half = n // 2
  first = find_number(r, c, half)
  second = find_number(r, c + half, half)
  third = find_number(r + half, c, half)
  fourth = find_number(r + half, c + half, half)

  new_arr = sorted([first, second, third, fourth])
  return new_arr[1]

print(find_number(0, 0, N))