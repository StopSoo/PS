# https://www.acmicpc.net/problem/15657

# 내 답안
# 걸린 시간: 52ms
# 백트래킹을 활용한 코드
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
numbers = sorted(list(map(int, input().strip().split())))
ans = []

def back():
  if len(ans) == M:
    print(*ans)
    return
  for number in numbers:
    if (not ans) or (ans and number >= ans[-1]):
      ans.append(number)
      back()
      ans.pop()

back()